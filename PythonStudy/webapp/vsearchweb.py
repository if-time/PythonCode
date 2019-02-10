from flask import Flask, render_template, request, redirect, escape
from vsearch import searchletters
import mysql.connector

app = Flask(__name__)

# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')


def log_request(req: 'flask_request', res: str) ->  None:
    with open('vsearch.log', 'a') as log:
        # print(req, res, file=log)
        # print(str(dir(req)), res, file=log)
        # print(req.form, file=log ,end='|')
        # print(req.remote_addr, file=log ,end='|')
        # print(req.user_agent, file=log ,end='|')
        # print(res, file=log)
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

def log_request_db(req: 'flask_request', res: str) ->  None:
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
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res, ))
    conn.commit()
    cursor.close()
    conn.close()

def log_request_db_with(req: 'flask_request', res: str) ->  None:
    dbconfig = {'host': '127.0.0.1',
		'user': 'vsearch',
		'password': 'vsearchpasswd',
		'database': 'vsearchlogDB', }
    with UseDatabase(dbconfig) as cursor:
         _SQL = """insert into log
    (phrase, letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res, ))

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(searchletters(phrase, letters))
    log_request(request, results)
    log_request_db(request, results)
    return render_template('results.html', the_phrase = phrase, the_letters = letters, the_result = results, the_title = title)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Dong')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    # return str(contents)
    return render_template('viewlog.html', the_title='View log', the_row_titles=titles, the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)