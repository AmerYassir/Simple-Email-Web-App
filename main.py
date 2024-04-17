import flask 
from flask import Flask, g,render_template,request
from data_base import EmailDB
from data_access import DataAccess
from data_writer import DataWriter

app=Flask(__name__)

email_db = EmailDB()
data_writer=DataWriter()
data_getter=DataAccess()


@app.route('/')
def signup():
    return render_template('sign_up.html')

@app.route('/signin')
def sign_in():
    return render_template('sign_in.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

@app.route('/draft')
def draft():
    return render_template('draft.html')

@app.route('/send',methods=['POST','GET'])
def send():
    reciver= request.form['to']
    subject= request.form['subject']
    message= request.form['message']
    
    return render_template('send.html')

@app.before_request
def before_request():
    g.db = email_db.get_db()

@app.teardown_request
def teardown_request(exception):
    email_db.close_db()

if __name__ == "__main__":
    email_db.init_db()
    app.run(debug=True)
