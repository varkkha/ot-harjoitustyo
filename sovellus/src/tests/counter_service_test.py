import unittest
import sqlite3
import os

from services.counter_service import CounterService
from repositories.counter_repository import CounterRepository
from repositories.user_repository import UserRepository
from entities.user import User

from dotenv import load_dotenv

class TestCounterService(unittest.TestCase):
    def setUp(self):
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env.test"))
        DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "test-database.sqlite"
        self.DATABASE_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", DATABASE_FILENAME)

        if os.path.exists(self.DATABASE_FILE_PATH):
            os.remove(self.DATABASE_FILE_PATH)

        self.connection = sqlite3.connect(self.DATABASE_FILE_PATH)

        self.user_repo = UserRepository(self.connection)
        self.repo = CounterRepository(self.connection)
        self.counter_service = CounterService(
            counter_repository=self.repo,
            user_repository=self.user_repo
        )

        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username,
                password
            )
        ''')
        cursor.execute('''
            CREATE TABLE calculations (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                acquisition_cost,
                tax_deduction,
                e_consumption,
                e_generation,
                e_purchase_price
            )
        ''')
        self.connection.commit()

    def test_net_consumption_is_calculated_correctly(self):
        e_consumption = 1000
        e_generation = 100
        net_consumption = self.counter_service.calculate_net_consumption(
            e_consumption, e_generation)
        self.assertEqual(net_consumption, 900)

    def test_save_calculation_saves_to_database(self):
        user = self.user_repo.create(User("testuser", "password123"))

        calc = self.counter_service.save_calculation(
            user=user,
            acquisition_cost=10600,
            tax_deduction=4000,
            e_consumption=21000,
            e_generation=7000,
            e_purchase_price=0.15
        )

        self.assertEqual(calc.user_id, user.user_id)
        self.assertEqual(calc.acquisition_cost, 10600)
        self.assertEqual(calc.tax_deduction, 4000)
        self.assertEqual(calc.e_consumption, 21000)
        self.assertEqual(calc.e_generation, 7000)
        self.assertEqual(calc.e_purchase_price, 0.15)

        results = self.repo.find_by_user_id(user.user_id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].acquisition_cost, 10600)

    def test_create_user(self):
        user = self.counter_service.create_user("testuser", "password123")

        result = self.counter_service.get_user()
        self.assertEqual(result.username, "testuser")

    def test_get_users(self):
        user1 = self.counter_service.create_user("testuser1", "password123")
        user2 = self.counter_service.create_user("testuser2", "password123")

        result = self.counter_service.get_users()
        self.assertEqual(len(result), 2)

    def test_succesful_login(self):
        self.counter_service.create_user("testuser", "secret123")

        logged = self.counter_service.login("testuser", "secret123")
        self.assertEqual(logged.username, "testuser")


