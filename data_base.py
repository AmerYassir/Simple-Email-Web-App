import sqlite3
from flask import g


class UserProperty:
    USER_ID = 0
    USERNAME = 1
    PASSWORD = 2
    EMAIL = 3

class MessageProperty:
    MESSAGE_ID = 0
    SENDER_ID = 1
    RECEIVER_ID = 2
    SUBJECT = 3
    BODY = 4
    CATEGORY = 5
    DATE = 6

class MessageCategory:
    INBOX = 'inbox'
    TRASH = 'trash'
    SPAM = 'spam'
    

class EmailDB:
    def __init__(self, db_name='email_app.db'):
        self.db_name = db_name

    def connect_db(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        with self.connect_db() as connection:
            with connection as c:
                c.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT,
                        email TEXT UNIQUE
                    )
                ''')

                c.execute('''
                    CREATE TABLE IF NOT EXISTS messages (
                        message_id INTEGER PRIMARY KEY,
                        sender_id INTEGER,
                        receiver_id INTEGER,
                        subject TEXT,
                        body TEXT,
                        category TEXT,
                        date DATETIME DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY(sender_id) REFERENCES users(user_id),
                        FOREIGN KEY(receiver_id) REFERENCES users(user_id)
                    )
                ''')


    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = self.connect_db()
        return db

    def close_db(self, exception=None):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

