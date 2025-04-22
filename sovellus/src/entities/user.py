"""User-luokka käyttäjän kuvaamista varten."""

class User:
    """Luokka, joka kuvaa käyttäjää.

    Attributes:
        username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
        password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
        user_id: Numeroarvo, joka yksilöi käyttäjän tietokannassa.
    """

    def __init__(self, username, password, user_id=None):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
            user_id: Numeroarvo, joka yksilöi käyttäjän tietokannassa.
                     Oletuksena None, jolloin user_id asetetaan tietokantaan tallennuksen jälkeen.
        """
        self.username = username
        self.password = password
        self.user_id = user_id
