from flask import Flask, g,render_template,request,flash,redirect,url_for
from data_base import EmailDB
from data_access import DataAccess
from data_writer import DataWriter,DuplicateEmailError


app=Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key


email_db = EmailDB()
email_db.init_db()

data_writer=DataWriter()
data_getter=DataAccess()

guser=10
@app.route('/')
def signup():
    return render_template('sign_up.html')

@app.route('/register',methods=['POST'])
def register():
    try:
        username= request.form['username']
        password= request.form['password']
        email= request.form['email']
        data_writer.write_user(username,password,email)
        flash('Registration successful!', 'success') 
        return redirect('/signin')
    except DuplicateEmailError as e:
        flash(str(e.message),'error')
    return redirect('/')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password_input = request.form['password']
    user = data_getter.get_user_by_username(username=username)
    
    if user:
        user_password = str(user[2])
        if user_password.lower() == password_input.lower():
            # Successful login, redirect to user's inbox
            return redirect(url_for('inbox', user_id=user[0]))
    
    # If login fails, you can render an error message or redirect to login page again
    return render_template('login.html', error="Invalid username or password")

@app.route('/signin')
def sign_in():
    return render_template('sign_in.html')

@app.route('/inbox')
def inbox():
    user_id=request.args.get('user_id')
    messages = data_getter.get_messages_by_user_id(user_id)
    print(messages)
    return render_template('inbox.html', messages=messages)

@app.route('/draft')
def draft():
    return render_template('draft.html')

@app.route('/send')
def send():
    
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
