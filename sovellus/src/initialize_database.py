from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id integer primary key,
            username text unique,
            password text
        );
    ''')

    cursor.execute('''
        CREATE TABLE calculations (
            id integer primary key,
            user_id integer,
            acquisition_cost,
            tax_deduction,
            e_consumption,
            e_generation,
            e_purchase_price,
            yearly_savings,
            payback_time,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
