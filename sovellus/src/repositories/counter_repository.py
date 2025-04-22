"""CounterRepository-luokka aurinkopaneelilaskureiden tietokantaoperaatioita varten."""

from database_connection import get_database_connection
from entities.counter import Counter

class CounterRepository:
    """Luokka, joka vastaa aurinkopaneelilaskureihin liittyvistä tietokantaoperaatioista.
    """
    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """
        self._connection = connection
        self._cursor = self._connection.cursor()

    def save_counter(self, counter):
        """Tallettaa aurinkopaneelilaskurin laskelman tietokantaan.

        Args:
            counter: Counter-olio, joka sisältää laskelman tiedot.

        Returns:
            Tallennettu Counter-olio.
        """

        self._cursor.execute('''
        INSERT INTO calculations (
            user_id,
            acquisition_cost,
            tax_deduction,
            e_consumption,
            e_generation,
            e_purchase_price
        )
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (counter.user_id,
          counter.acquisition_cost,
          counter.tax_deduction,
          counter.e_consumption,
          counter.e_generation,
          counter.e_purchase_price
        ))

        self._connection.commit()

        return counter

    def get_all_calculations(self):
        """Palauttaa kaikki tietokannassa olevat aurinkopaneelilaskelmat.

        Returns:
            counters: Lista Counter-olioita, jotka kuvaavat tallennettuja laskelmia.
        """
        self._cursor.execute("SELECT * FROM calculations")
        rows = self._cursor.fetchall()

        counters = []
        for row in rows:

            counter = Counter(
                acquisition_cost=row[2],
                tax_deduction=row[3],
                e_consumption=row[4],
                e_generation=row[5],
                e_purchase_price=row[6],
                user_id=row[1],
                counter_id=row[0]
            )

            counters.append(counter)

        return counters

    def find_by_user_id(self, user_id):
        """Palauttaa tietyn käyttäjän laskelmat user_id:n perusteella.

        Args:
            user_id: Käyttäjän yksilöivä tunniste.

        Returns:
            counters: Lista Counter-olioita, jotka kuvaavat käyttäjän tallentamia laskelmia.
        """
        query = "SELECT * FROM calculations WHERE user_id = ?"
        cursor = self._connection.cursor()
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()

        counters = []
        for row in rows:

            counter = Counter(
                acquisition_cost=row[2],
                tax_deduction=row[3],
                e_consumption=row[4],
                e_generation=row[5],
                e_purchase_price=row[6],
                user_id=row[1],
                counter_id=row[0]
            )

            counters.append(counter)

        return counters

    def delete(self, counter_id):
        """Poistaa tietyn laskelman tietokannasta.

        Args:
            counter_id: Poistettavan laskelman id.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM calculations WHERE id = ?", (counter_id,))
        self._connection.commit()

counter_repository = CounterRepository(get_database_connection())
