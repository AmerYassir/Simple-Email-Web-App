import sqlite3
from flask import g

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

