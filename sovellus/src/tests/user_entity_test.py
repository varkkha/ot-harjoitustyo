import unittest
from entities.user import User

class TestCounter(unittest.TestCase):

    def setUp(self):
        self.user = User(
            username="Testikäyttäjä",
            password="Salasana",
            user_id=1
        )

    def test_initialization(self):
        self.assertEqual(self.user.username, "Testikäyttäjä")
        self.assertEqual(self.user.password, "Salasana")
        self.assertEqual(self.user.user_id, 1)