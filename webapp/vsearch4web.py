from flask import Flask, render_template, request, escape
from searchmodule import search_for_letters

from DBcm import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1', 'port': '3307', 'user': 'vsearch', 'password': 'password123', 'database': 'vsearchlogDB', }

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters website!')


def log_request(req: 'flask_request', res: str) -> None:
   
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """INSERT INTO log (phrase, letters, ip, browser_string, results) VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, str(req.user_agent), res, ))

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase = phrase, the_letters=letters, the_title=title, the_results=results,)


@app.route('/viewlog')
def view_the_log() -> 'html':

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        titles = ('Fraza', 'Litery', 'Adres klienta', 'Agent użytkownika', 'Wyniki')

    return render_template('viewlog.html', the_title='Widok logu', the_row_titles=titles, the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)