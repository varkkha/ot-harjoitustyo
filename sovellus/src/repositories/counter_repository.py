from database_connection import get_database_connection

class CounterRepository:

    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()

    def save_counter(self, counter):

        self._cursor.execute('''
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

    def get_all_calculations(self):
        self._cursor.execute("SELECT * FROM calculations")
        return self._cursor.fetchall()

counter_repository = CounterRepository(get_database_connection())
