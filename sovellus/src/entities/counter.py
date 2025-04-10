class Counter:
    def __init__(self,
                 acquisition_cost,
                 tax_deduction,
                 e_consumption,
                 e_generation,
                 e_purchase_price,
                 user_id):
        self.user_id = user_id
        self.acquisition_cost = acquisition_cost
        self.tax_deduction = tax_deduction
        self.e_consumption = e_consumption
        self.e_generation = e_generation
        self.e_purchase_price = e_purchase_price

        self.yearly_savings = self.calculate_savings(e_generation, e_purchase_price)
        self.payback_time = self.calculate_payback_time(
            self.acquisition_cost - self.tax_deduction, self.yearly_savings)

    def calculate_savings(self, e_generation, e_purchase_price):
        return e_generation * e_purchase_price

    def calculate_payback_time(self, net_cost, yearly_savings):
        return net_cost / yearly_savings
