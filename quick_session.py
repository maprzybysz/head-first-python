from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'secretkeyxd123'

@app.route('/setuser/<user>')
def setuser(user: str) -> str: 
    session['user'] = user
    return 'The user is: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'The user is: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)