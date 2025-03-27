from services.counter_service import CounterService

acquisition_cost = 10600
tax_deduction = 4000
e_consumption = 21000
e_generation = 7000
e_purchase_price = 0.15

calculator = CounterService()
savings, payback_time = calculator.calculate(acquisition_cost, tax_deduction, e_generation, e_purchase_price)

print(f"Annual savings: {savings:.2f} eur")
print(f"Payback time: {payback_time:.1f} years")

