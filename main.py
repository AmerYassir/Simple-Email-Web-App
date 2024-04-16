import flask 
from flask import render_template
app=flask.Flask(__name__)

@app.route('/inbox')
@app.route('/')
def inbox():
    return render_template('inbox.html')

@app.route('/draft')
def draft():
    return render_template('draft.html')

@app.route('/send')
def send():
    return render_template('send.html')
