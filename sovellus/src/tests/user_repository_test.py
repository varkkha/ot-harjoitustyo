import unittest
import sqlite3
import os

from repositories.user_repository import UserRepository
from entities.user import User
from dotenv import load_dotenv

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env.test"))
        DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "test-database.sqlite"
        self.DATABASE_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", DATABASE_FILENAME)

        if os.path.exists(self.DATABASE_FILE_PATH):
            os.remove(self.DATABASE_FILE_PATH)

        self.connection = sqlite3.connect(self.DATABASE_FILE_PATH)
        self.repo = UserRepository(self.connection)

        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username,
                password
            )
        ''')
        self.connection.commit()

    def test_delete_all(self):
        user1 = User(username="testuser1", password="password1")
        user2 = User(username="testuser2", password="password2")

        self.repo.create(user1)
        self.repo.create(user2)

        result1 = self.repo.find_all()

        self.assertEqual(len(result1), 2)

        self.repo.delete_all()

        result2 = self.repo.find_all()

        self.assertEqual(len(result2), 0)

    def test_find_by_username_returns_none_if_user_not_found(self):
        result = self.repo.find_by_username("empty")
        self.assertIsNone(result)


