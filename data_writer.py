import sqlite3

class DuplicateEmailError(Exception):
    '''
    a class working as error message creator
    it handles when duplicated user email or username are entered
    '''
    def __init__(self, message="Email address /Username already in use!"):
        self.message = message
        super().__init__(self.message)


class DataWriter:
    def __init__(self, db_name='email_app.db'):
        self.db_name = db_name
        self.msg_count = 0

    def write_user(self, username, password, email):
        '''
        open connection with the databse and insert 
        user into users table and handle duplicated users
        '''
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                               (username, password, email))

            print("User data successfully written to the database.")
        except sqlite3.Error as e:
            print("Error writing user data to the database:", e)
            raise DuplicateEmailError()
            

    def write_message(self, sender_id, receiver_id, subject, body):
        '''
        open connection with the databse and insert 
        message into messages table 
        '''
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                cursor.execute("INSERT INTO messages (sender_id, receiver_id, subject, body) VALUES (?, ?, ?, ?)",
                               (sender_id, receiver_id, subject, body))

            print("Message data successfully written to the database.")
            self.msg_count+=1
        except sqlite3.Error as e:
            print("Error writing message data to the database:", e)

