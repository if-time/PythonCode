from flask import Flask, render_template, request, redirect
from vsearch import searchletters

app = Flask(__name__)

# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(searchletters(phrase, letters))
    return render_template('results.html', the_phrase = phrase, the_letters = letters, the_result = results, the_title = title)

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Dong')

app.run(debug=True)