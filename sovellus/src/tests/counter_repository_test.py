import unittest
import sqlite3
import os

from repositories.counter_repository import CounterRepository
from entities.counter import Counter
from dotenv import load_dotenv

class TestCounterRepository(unittest.TestCase):
    def setUp(self):
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env.test"))
        DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "test-database.sqlite"
        self.DATABASE_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", DATABASE_FILENAME)

        if os.path.exists(self.DATABASE_FILE_PATH):
            os.remove(self.DATABASE_FILE_PATH)

        self.connection = sqlite3.connect(self.DATABASE_FILE_PATH)
        self.repo = CounterRepository(self.connection)

        cursor = self.connection.cursor()
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

    def test_save_and_get_all(self):
        counter = Counter(
            user_id=1,
            acquisition_cost=10600,
            tax_deduction=4000,
            e_consumption=21000,
            e_generation=7000,
            e_purchase_price=0.15
        )

        self.repo.save_counter(counter)
        counters = self.repo.get_all_calculations()

        self.assertEqual(len(counters), 1)
        self.assertEqual(counters[0].acquisition_cost, 10600)
        self.connection.close()

    def test_find_by_user_id(self):
        counter1 = Counter(
            user_id=1,
            acquisition_cost=10600,
            tax_deduction=4000,
            e_consumption=21000,
            e_generation=7000,
            e_purchase_price=0.15
        )

        counter2 = Counter(
            user_id=2,
            acquisition_cost=10600,
            tax_deduction=4000,
            e_consumption=21000,
            e_generation=7000,
            e_purchase_price=0.15
        )

        self.repo.save_counter(counter1)
        self.repo.save_counter(counter2)

        result = self.repo.find_by_user_id(2)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].user_id, 2)
        self.connection.close()

    def test_delete_counter(self):
        counter1 = Counter(
            user_id=1,
            acquisition_cost=10600,
            tax_deduction=4000,
            e_consumption=21000,
            e_generation=7000,
            e_purchase_price=0.15
        )

        counter2 = Counter(
            user_id=2,
            acquisition_cost=10600,
            tax_deduction=4000,
            e_consumption=21000,
            e_generation=7000,
            e_purchase_price=0.15
        )

        self.repo.save_counter(counter1)
        self.repo.save_counter(counter2)
        self.repo.delete(2)
        counters = self.repo.get_all_calculations()

        self.assertEqual(len(counters), 1)
        self.assertEqual(counters[0].user_id, 1)
        result = self.repo.find_by_user_id(2)
        self.assertEqual(len(result), 0)
        self.connection.close()
