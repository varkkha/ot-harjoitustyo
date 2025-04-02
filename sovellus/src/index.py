from services.counter_service import CounterService
from database_connection import get_database_connection

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

connection = get_database_connection()
cursor = connection.cursor()

cursor.execute('''
    INSERT INTO calculations (acquisition_cost, tax_deduction, e_consumption, e_generation, e_purchase_price, yearly_savings, payback_time)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', (acquisition_cost, tax_deduction, e_consumption, e_generation, e_purchase_price, savings, payback_time))

connection.commit()

cursor.execute("SELECT * FROM calculations")
rows = cursor.fetchall()

print("\nSaved calculations in the database:")
for row in rows:
    print(dict(row))

connection.close()
