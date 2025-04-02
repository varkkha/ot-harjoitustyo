from entities.counter import Counter
from database_connection import get_database_connection

class CounterRepository:

    def __init__(self, connection):

        self._connection = connection

    def save_counter(self, counter):

        cursor = self._connection.cursor()

        cursor.execute('''
        INSERT INTO calculations (
                       acquisition_cost,
                       tax_deduction,
                       e_consumption,
                       e_generation,
                       e_purchase_price,
                       yearly_savings,
                       payback_time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (counter.acquisition_cost,
          counter.tax_deduction,
          counter.e_consumption,
          counter.e_generation,
          counter.e_purchase_price,
          counter.yearly_savings,
          counter.payback_time))

        self._connection.commit()

        return counter

counter_repository = CounterRepository(get_database_connection())
