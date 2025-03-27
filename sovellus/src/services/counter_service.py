class CounterService:
    def __init__(self):
        pass

    def calculate_net_consumption(self, e_consumption, e_generation):
        return e_consumption - e_generation

    def calculate_savings(self, e_generation, e_purchase_price):
        return e_generation * e_purchase_price

    def calculate_payback_time(self, net_cost, yearly_savings):
        return net_cost / yearly_savings

    def calculate(self, acquisition_cost, tax_deduction, e_generation, e_purchase_price):
        net_cost = acquisition_cost - tax_deduction
        yearly_savings = self.calculate_savings(e_generation, e_purchase_price)
        payback_time = self.calculate_payback_time(net_cost, yearly_savings)
        return yearly_savings, payback_time

