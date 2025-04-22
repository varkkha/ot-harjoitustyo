"""Sovelluslogiikasta vastaavat luokat."""

from entities.counter import Counter
from entities.user import User

from repositories.counter_repository import (
    counter_repository as default_counter_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class CounterService:
    """Luokka, joka vastaa sovelluslogiikasta aurinkopaneelilaskurissa."""

    def __init__(
        self,
        counter_repository=default_counter_repository,
        user_repository=default_user_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            counter_repository:
            Vapaaehtoinen, oletusarvoisesti CounterRepository-olio.
            Olio, joka vastaa laskelmien tallennuksesta ja hakemisesta.
            user_repository:
            Vapaaehtoinen, oletusarvoisesti UserRepository-olio.
            Olio, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista.
        """
        self._user = None
        self._counter_repository = counter_repository
        self._user_repository = user_repository

    def calculate_net_consumption(self, e_consumption, e_generation):
        """Laskee nettokulutuksen.

        Args:
            e_consumption: Sähkön vuosittainen kulutus (kWh).
            e_generation: Oman aurinkopaneelin vuosittainen sähköntuotto (kWh).

        Returns:
            Nettokulutus (sähkönkulutus - sähköntuotto)
        """
        return e_consumption - e_generation

    def save_calculation(self,
                         user,
                         acquisition_cost,
                         tax_deduction,
                         e_consumption,
                         e_generation,
                         e_purchase_price):
        """Tallentaa käyttäjän aurinkopaneelilaskelman tietokantaan.

        Args:
            user: Käyttäjä, jolle laskelma kuuluu.
            acquisition_cost: Aurinkopaneelien hankintahinta (eur).
            tax_deduction: Kotitalousvähennys hankintahinnasta (eur).
            e_consumption: Vuosittainen sähkönkulutus (kWh).
            e_generation: Vuosittainen sähköntuotto (kWh).
            e_purchase_price: Sähkön ostohinta (eur/kWh).

        Returns:
            Counter: Tallennettu laskelma Counter-oliona.
        """
        calculation = Counter(
            acquisition_cost=acquisition_cost,
            tax_deduction=tax_deduction,
            e_consumption=e_consumption,
            e_generation=e_generation,
            e_purchase_price=e_purchase_price,
            user_id=user.user_id
        )

        return self._counter_repository.save_counter(calculation)

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja kirjaa tarvittaessa sisään.

        Args:
            username:
            Käyttäjän käyttäjätunnus (merkkijonoarvo)
            password:
            Käyttäjän salasana (merkkijonoarvo)
            login:
            Vapaaehtoinen, oletusarvo True.
            Kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen (boolean).

        Raises:
            UsernameExistsError:
            Virhe, joka heitetään, jos käyttäjätunnus on jo olemassa.

        Returns:
            Luotu käyttäjä User-olion muodossa.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Käyttäjätunnus {username} on jo käytössä")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        if not user:
            print("Käyttäjää ei löydy.")
            raise InvalidCredentialsError("Virheellinen käyttäjätunnus tai salasana")

        if user.password != password:
            print("Salasana väärin.")
            raise InvalidCredentialsError("Virheellinen käyttäjätunnus tai salasana")

        self._user = user

        return user

    def get_user(self):
        """Palauttaa tällä hetkellä sisäänkirjatun käyttäjän.

        Returns:
            User: Tällä hetkellä sisäänkirjatun käyttäjän User-olio.
                  Jos käyttäjää ei ole kirjautuneena, palautetaan None.
        """

        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät tietokannasta.

        Returns:
            User-oliota sisältä lista kaikista tietokannassa olevista käyttäjistä.
        """

        return self._user_repository.find_all()

    def get_previous_calculations(self, user):
        """Palauttaa kaikki aiemmat laskelmat annetulle käyttäjälle.

        Args:
            user: Käyttäjä, jonka aiemmat laskelmat haetaan.

        Returns:
            Lista käyttäjän aiemmista laskelmista Counter-olioina.
        """

        return self._counter_repository.find_by_user_id(user.user_id)

    def delete_counter(self, counter_id):
        """Poistaa laskelman tietokannasta.

        Args:
            counter_id: Poistettavan laskelman id.

        Returns:
           Palauttaa True, jos laskelman poistaminen onnistui, muuten False.
        """
        return self._counter_repository.delete(counter_id)

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos sovelluksesta."""

        self._user = None

counter_service = CounterService()
