"""UserRepository-luokka käyttäjien tietokantaoperaatioita varten."""

from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    """Luo User-olion tietokantarivistä.

    Args:
        row: Tietokantarivi, joka sisältää käyttäjän tiedot.

    Returns:
        User-olio, jossa on rivin tiedot, tai None jos rivi on tyhjä.
    """
    if not row:
        return None
    user = User(row[1], row[2])
    user.user_id = row[0]
    return user

class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus, jonka perusteella käyttäjä palautetaan.

        Returns:
            Palauttaa User-olion, jos käyttäjätunnus löytyy tietokannasta.
            Muussa tapauksessa palauttaa None.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """Tallentaa uuden käyttäjän tietokantaan.

        Args:
            user: User-olio, joka sisältää tallennettavan käyttäjän tiedot.

        Returns:
            User: Sama User-olio, johon on lisätty tietokannasta saatu user_id.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        user.user_id = cursor.lastrowid

        return user

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta."""

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
