import sqlite3

class DataAccess:
    def __init__(self, db_name='email_app.db'):
        self.db_name = db_name

    def get_user_by_email(self, email):
        '''
        open connection with the databse and retrive 
        user info by email from users table and returns None when user not found
        '''
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE email=?", (email,))
                user = cursor.fetchone()
                return user
        except sqlite3.Error as e:
            print("Error accessing user data from the database:", e)
            return None
 
    def get_user_by_id(self, user_id):
        '''
        open connection with the databse and retrive 
        user info by id from users table and returns None when user not found
        '''
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
                user = cursor.fetchone()
                return user
        except sqlite3.Error as e:
            print("Error accessing user data from the database:", e)
            return None

    def get_messages_by_user_id(self, user_id):
        '''
        open connection with the databse and retrive 
        user recived messages by id from messages table 
        and returns empty list when no messages found
        '''
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM messages WHERE receiver_id=? ORDER BY date DESC", (user_id,))
                messages = cursor.fetchall()#get all recived messages
                return messages
        except sqlite3.Error as e:
            print("Error accessing messages data from the database:", e)
            return []
    def get_messages_by_msg_id(self, msg_id):
        '''
        open connection with the databse and retrive 
        message by id from messages table 
        and returns empty list if any error happens
        '''
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM messages WHERE message_id=?", (msg_id,))
                message = cursor.fetchone()#get all recived messages
                return message
        except sqlite3.Error as e:
            print("Error accessing messages data from the database:", e)
            return None
