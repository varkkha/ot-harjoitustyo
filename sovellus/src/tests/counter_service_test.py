import unittest
from services.counter_service import CounterService

class TestCounterService(unittest.TestCase):
    def setUp(self):
        self.counter_service = CounterService()

    def test_net_consumption_is_calculated_correctly(self):
        e_consumption = 1000
        e_generation = 100
        net_consumption = self.counter_service.calculate_net_consumption(e_consumption, e_generation)
        self.assertEqual(net_consumption, 900)

    def test_savings_are_calculated_correctly(self):
        e_generation = 100
        e_purchase_price = 10
        savings = self.counter_service.calculate_savings(e_generation, e_purchase_price)
        self.assertEqual(savings, 1000)

    def test_paypack_time_is_calculated_correctly(self):
        net_cost = 100
        yearly_savings = 20
        payback_time = self.counter_service.calculate_payback_time(net_cost, yearly_savings)
        self.assertEqual(payback_time, 5)

    def test_savings_and_paypack_time_are_calculated_correctly(self):
        acquisition_cost = 1100
        tax_deduction = 100
        e_generation = 1000
        e_purchase_price = 1
        yearly_savings, payback_time = self.counter_service.calculate(acquisition_cost, tax_deduction, e_generation, e_purchase_price)
        self.assertEqual((yearly_savings, payback_time), (1000, 1))