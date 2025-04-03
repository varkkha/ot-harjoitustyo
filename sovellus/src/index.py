from services.counter_service import CounterService
from repositories.user_repository import user_repository
from repositories.counter_repository import counter_repository
from entities.user import User
from entities.counter import Counter

username = input("Create username: ")
password = input("Create password: ")

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

print(f"\nAnnual savings: {savings:.2f} eur")
print(f"Payback time: {payback_time:.1f} years")

new_user = User(username=username, password=password)
new_user = user_repository.create(new_user)
user_id = new_user.id

new_counter = Counter(
    acquisition_cost=acquisition_cost,
    tax_deduction=tax_deduction,
    e_consumption=e_consumption,
    e_generation=e_generation,
    e_purchase_price=e_purchase_price
)

counter_repository.save_counter(new_counter, user_id)

calculations = counter_repository.get_all_calculations()
print("\nSaved calculations in the database:")
for row in calculations:
    print(dict(row))
