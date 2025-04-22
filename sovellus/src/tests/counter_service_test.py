import unittest
from services.counter_service import CounterService

class TestCounterService(unittest.TestCase):
    def setUp(self):
        self.counter_service = CounterService()

    def test_net_consumption_is_calculated_correctly(self):
        e_consumption = 1000
        e_generation = 100
        net_consumption = self.counter_service.calculate_net_consumption(
            e_consumption, e_generation)
        self.assertEqual(net_consumption, 900)

