from services.counter_service import CounterService

acquisition_cost = float(input("Enter acquisition cost: "))
tax_deduction = float(input("Enter tax deduction: "))
e_consumption = float(input("Enter energy consumption: "))
e_generation = float(input("Enter energy generation: "))
e_purchase_price = float(input("Enter energy purchase price (per unit): "))

calculator = CounterService()
savings, payback_time = calculator.calculate(
    acquisition_cost,
    tax_deduction,
    e_generation,
    e_purchase_price
)

print(f"Annual savings: {savings:.2f} eur")
print(f"Payback time: {payback_time:.1f} years")
