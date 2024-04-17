from flask import Flask, g,render_template,request,flash,redirect
from data_base import EmailDB
from data_access import DataAccess
from data_writer import DataWriter,DuplicateEmailError


app=Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key


email_db = EmailDB()
email_db.init_db()

data_writer=DataWriter()
data_getter=DataAccess()


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
@app.route('/signin')
def sign_in():
    return render_template('sign_in.html')

@app.route('/inbox')
def inbox():
    return render_template('inbox.html')

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
