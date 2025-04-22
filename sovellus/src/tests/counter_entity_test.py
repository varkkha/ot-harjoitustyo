import unittest
from entities.counter import Counter

class TestCounter(unittest.TestCase):

    def setUp(self):
        self.counter = Counter(
            acquisition_cost=10600,
            tax_deduction=4000,
            e_consumption=21000,
            e_generation=7000,
            e_purchase_price=0.15,
            user_id=1
        )

    def test_initialization(self):
        self.assertEqual(self.counter.acquisition_cost, 10600)
        self.assertEqual(self.counter.tax_deduction, 4000)
        self.assertEqual(self.counter.e_consumption, 21000)
        self.assertEqual(self.counter.e_generation, 7000)
        self.assertEqual(self.counter.e_purchase_price, 0.15)
        self.assertEqual(self.counter.user_id, 1)

    def test_yearly_savings(self):
        savings = self.counter.e_generation * self.counter.e_purchase_price
        self.assertEqual(self.counter.yearly_savings, savings)

    def test_payback_time(self):
        net_cost = self.counter.acquisition_cost - self.counter.tax_deduction
        payback_time = net_cost / self.counter.yearly_savings
        self.assertEqual(self.counter.payback_time, payback_time)

    def test_payback_time_if_e_generation_is_zero(self):
        self.counter.e_generation = 0
        self.assertEqual(self.counter.payback_time, float('inf'))