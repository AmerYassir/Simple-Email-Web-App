from flask import Flask, g, render_template, request, flash, redirect, url_for, session
from data_base import EmailDB
from data_access import DataAccess
from data_writer import DataWriter, DuplicateEmailError
import re

app = Flask(__name__)


app.config['SECRET_KEY'] = 'email-web-app#amer'

# Initialize the email database
email_db = EmailDB()
email_db.init_db()

# Initialize data writer and data access objects
data_writer = DataWriter()
data_getter = DataAccess()

# Function to validate username format
def validate_username(username):
    '''
    Define the regular expression pattern
    Matches any string of length 4 or more 
    containing at least one alphabetic character
    '''
    pattern = r'^(?=.*[a-zA-Z]).{4,}$'  

    # Use re.match to check if the username matches the pattern
    if re.match(pattern, username):
        return True
    else:
        return False

# Sign-up route
@app.route('/')
def signup():
    # Render the sign-up page
    return render_template('sign_up.html', data=None)

# Registration route
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if not validate_username(username):
            flash("Invalid username. Username must be at least 4 characters long and contain alphabetic characters.", 'error')
            return redirect('/')
        # Write user data to the database
        data_writer.write_user(username, password, email.lower())
        return redirect('/signin')
    except DuplicateEmailError as e:
        flash(str(e.message), 'error')
    return redirect('/')

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form['user-email']
    password_input = request.form['password']
    user = data_getter.get_user_by_email(email=email.lower())
    
    if user:
        user_password = str(user[2])
        if user_password == password_input:
            session.clear()
            # Successful login, redirect to user's inbox
            return redirect(url_for('inbox', user_id=user[0]))
    
    # If login fails, render the sign-in page again
    return render_template('sign_in.html', data=None)

# Sign-in route
@app.route('/signin')
def sign_in():
    return render_template('sign_in.html', data=None)

@app.route('/inbox/<int:email_id>')
def view_email(email_id):
    message_id,sender_id,reciveir_id,subject,body,date=data_getter.get_messages_by_msg_id(email_id)
    sender_email=data_getter.get_user_by_id(sender_id)[3]
    reciveir_email=data_getter.get_user_by_id(reciveir_id)[3]
    email={'message_id':message_id,'sender_email':sender_email,
          'reciveir_email':reciveir_email,'subject':subject,'body':body,'date':date}
    return render_template('email_body.html',email=email,user_info=session.get('user_info'))
# Inbox route
@app.route('/inbox')
def inbox():

    if not session.get('user_id'):
        user_id = request.args.get('user_id')
        session['user_id'] = user_id 
    if not session.get('user_info'):
        user_info =data_getter.get_user_by_id(user_id) 
        session['user_info']=user_info

    user_id = session.get('user_id')
    user_info = session.get('user_info')
    messages = data_getter.get_messages_by_user_id(user_id)
    email_covers=[]
    for message_id,sender_id,_,subject,_,_ in messages:
        sender_name=data_getter.get_user_by_id(sender_id)[1]
        email_covers.append({'sender_name':sender_name,'subject':subject,'message_id':message_id})
    user_info = data_getter.get_user_by_id(user_id)
    return render_template('inbox.html', email_covers=email_covers, user_info=user_info)

# Draft route
@app.route('/draft')
def draft():
    return render_template('draft.html')

# Send route
@app.route('/send', methods=["POST", 'GET'])
def send():

    if request.method == "POST":

        # get reciver email we want to send email to
        reciver_name = request.form['to']
        #check if email does exist and retrive it's info
        user = data_getter.get_user_by_email(reciver_name)
        if not user: # display error message when reciver email doesn't exist
            flash("Non-existing user email", 'error')
            return render_template('send.html',user_info=session.get('user_info'))
        reciver_id = user[0]
        msg_subject = request.form['subject']
        msg_body = request.form['message']
        # Write message data to the database
        data_writer.write_message(session.get('user_id'), reciver_id, msg_subject, msg_body)
        return render_template('send.html', data=None,user_info=session.get('user_info'))
    else:
        return render_template('send.html', data=None,user_info=session.get('user_info'))

# Run setup before each request
@app.before_request
def before_request():
    g.db = email_db.get_db()

# Run teardown after each request
@app.teardown_request
def teardown_request(exception):
    email_db.close_db()

# Run the Flask app
if __name__ == "__main__":
    email_db.init_db()
    app.run(debug=True)
