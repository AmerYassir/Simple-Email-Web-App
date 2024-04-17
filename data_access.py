import sqlite3

class DataAccess:
    def __init__(self, db_name='email_app.db'):
        self.db_name = db_name

    def get_user_by_username(self, username):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=?", (username,))
                user = cursor.fetchone()
                return user
        except sqlite3.Error as e:
            print("Error accessing user data from the database:", e)
            return None

    def get_messages_by_user_id(self, user_id):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM messages WHERE receiver_id=?", (user_id,))
                messages = cursor.fetchall()
                return messages
        except sqlite3.Error as e:
            print("Error accessing messages data from the database:", e)
            return []
