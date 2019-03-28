from flask import Flask, render_template, request, redirect, escape, session, copy_current_request_context
from vsearch import searchletters
import mysql.connector
from DBcm import UseDatabase, ConnectionError
from checker import check_logged_in
from threading import Thread
from time import sleep

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }
app.secret_key = '1234567890'
# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        # print(req, res, file=log)
        # print(str(dir(req)), res, file=log)
        # print(req.form, file=log ,end='|')
        # print(req.remote_addr, file=log ,end='|')
        # print(req.user_agent, file=log ,end='|')
        # print(res, file=log)
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


def log_request_db(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results"""
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                          req.remote_addr, req.user_agent.browser, res, ))
    conn.commit()
    cursor.close()
    conn.close()


def log_request_db_with(req: 'flask_request', res: str) -> None:
    raise Exception("Something awful just happened.")
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                          req.remote_addr, req.user_agent.browser, res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    
    # log_request_db(request, results)
    # log_request_db_with(request, results)
    @copy_current_request_context
    def log_request_db_with(req: 'flask_request', res: str) -> None:
        sleep(15)
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                            req.remote_addr, req.user_agent.browser, res, ))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(searchletters(phrase, letters))
    try:
        # log_request(request, results)
        t = Thread(target=log_request_db_with, args=(request, results))
        t.start()
    except Exception as err:
        print('*****Logging failed with this error: ', str(err))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_result=results, the_title=title)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Dong')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    # contents = []
    # with open('vsearch.log') as log:
    #     for line in log:
    #         contents.append([])
    #         for item in line.split('|'):
    #             contents[-1].append(escape(item))
    # titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    """Display the contents of the log file as a HTML table."""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        # return str(contents)
        return render_template('viewlog.html',
                               the_title='View log',
                               the_row_titles=titles,
                               the_data=contents,)
    except ConnectionError as err:
        print("Is your database switched on? Error: ", str(err))


if __name__ == '__main__':
    app.run(debug=True)
