import sqlite3
from data_base import MessageCategory
from spam_detector import spam_detector
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
        self.detector=spam_detector()

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

        except sqlite3.Error as e:
            raise DuplicateEmailError()
            

    def write_message(self, sender_id, receiver_id, subject, body,category=MessageCategory.INBOX):
        '''
        open connection with the databse and insert 
        message into messages table 
        '''
        try:
            is_spam=self.detector.test_message(body)
            if is_spam:
                category=MessageCategory.SPAM
        except:   
            pass
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                cursor.execute("INSERT INTO messages (sender_id, receiver_id, subject, body,category) VALUES (?, ?, ?, ?,?)",
                               (sender_id, receiver_id, subject, body,category))
            self.msg_count+=1
        except sqlite3.Error as e:
            pass

    def update_message(self,message_id,column,new_value):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query="""UPDATE messages SET %s=? 
                                WHERE message_id=?"""%column
                cursor.execute(query, (new_value, message_id))
  
        except sqlite3.Error as e:
            pass
    
    def delete_message(self,message_id):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                query = "DELETE FROM messages WHERE message_id = ?"
                cursor.execute(query, (str(message_id)))

        except sqlite3.Error as e:
            pass

    
 

