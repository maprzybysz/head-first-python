from flask import Flask 
from searchmodule import search_for_letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello, world, here flask!'


@app.route('/search4')
def do_search() -> str:
    return str(search_for_letters('zycie, wszechswiat i cala reszta', 'eiru,!'))

app.run()