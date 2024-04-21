from flask import Flask, g,render_template,request,flash,redirect,url_for,session
from data_base import EmailDB
from data_access import DataAccess
from data_writer import DataWriter,DuplicateEmailError
import re

app=Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key


email_db = EmailDB()
email_db.init_db()

data_writer=DataWriter()
data_getter=DataAccess()

def validate_username(username):
    # Define the regular expression pattern
    pattern = r'^(?=.*[a-zA-Z]).{4,}$'  # Matches any string of length 8 or more containing at least one alphabetic character

    # Use re.match to check if the username matches the pattern
    if re.match(pattern, username):
        return True
    else:
        return False

@app.route('/')
def signup():
    return render_template('sign_up.html',data=None)

@app.route('/register',methods=['POST'])
def register():
    try:
        username= request.form['username']
        password= request.form['password']
        email= request.form['email']
        if not validate_username(username):
            flash("Invalid username. Username must be at least 4 characters long and contain alphabetic characters.",'error')
            return redirect('/')
        data_writer.write_user(username,password,email.lower())
        return redirect('/signin')
    except DuplicateEmailError as e:
        flash(str(e.message),'error')
    return redirect('/')

@app.route('/login',methods=['POST'])
def login():
    email = request.form['user-email']
    password_input = request.form['password']
    user = data_getter.get_user_by_email(email=email.lower())
    
    if user:
        user_password = str(user[2])
        if user_password== password_input:
            # Successful login, redirect to user's inbox
            return redirect(url_for('inbox', user_id=user[0]))
    
    # If login fails, you can render an error message or redirect to login page again
    return render_template('sign_in.html',data=None)

@app.route('/signin')
def sign_in():
    return render_template('sign_in.html',data=None)

@app.route('/inbox')
def inbox():
    user_id=request.args.get('user_id')
    session['user_id']=user_id
    messages = data_getter.get_messages_by_user_id(user_id)

    return render_template('inbox.html', messages=messages)

@app.route('/draft')
def draft():
    return render_template('draft.html')


@app.route('/send',methods=["POST",'GET'])
def send():
    if request.method=="POST":
        reciver_name=request.form['to']
        print(reciver_name)
        user =data_getter.get_user_by_email(reciver_name)
        if not user:
            flash("non exsiting user email",'error')
            return render_template('send.html')
        reciver_id= user[0]
        msg_subject=request.form['subject']
        msg_body=request.form['message']
        data_writer.write_message(session.get('user_id'),reciver_id,msg_subject,msg_body)
        return render_template('send.html',data=None)
        
    else:
        return render_template('send.html',data=None)

@app.before_request
def before_request():
    g.db = email_db.get_db()

@app.teardown_request
def teardown_request(exception):
    email_db.close_db()

if __name__ == "__main__":
    email_db.init_db()
    app.run(debug=True)
