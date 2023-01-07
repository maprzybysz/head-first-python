from flask import Flask, render_template, request, escape
from searchmodule import search_for_letters
import datetime;

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters website!')


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(datetime.datetime.now(), req.form, req.remote_addr, req.user_agent, req.user_agent, res, file=log, sep='|')


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
    contents = []
    with open('vsearch.log') as log:
       for line in log:
        contents.append([])
        for item in line.split('|'):
            contents[-1].append(escape(item))
    titles = ('Data', 'Dane z formularza', 'Adres klienta', 'Agent użytkownika', 'Wyniki')
    return render_template('viewlog.html', the_title='Widok logu', the_row_titles=titles, the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)