import sqlite3

class DuplicateEmailError(Exception):
    def __init__(self, message="Email address /Username already in use!"):
        self.message = message
        super().__init__(self.message)


class DataWriter:
    def __init__(self, db_name='email_app.db'):
        self.db_name = db_name

    def write_user(self, username, password, email):
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
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                cursor.execute("INSERT INTO messages (sender_id, receiver_id, subject, body) VALUES (?, ?, ?, ?)",
                               (sender_id, receiver_id, subject, body))

            print("Message data successfully written to the database.")
        except sqlite3.Error as e:
            print("Error writing message data to the database:", e)

