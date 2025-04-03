import hashlib
from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):

        hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, hashed_password)
        )

        self._connection.commit()

        user.id = cursor.lastrowid

        return user

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
