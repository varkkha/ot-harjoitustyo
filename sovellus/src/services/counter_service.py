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
    def __init__(
        self,
        counter_repository=default_counter_repository,
        user_repository=default_user_repository
    ):
        self._user = None
        self._counter_repository = counter_repository
        self._user_repository = user_repository

    def calculate_net_consumption(self, e_consumption, e_generation):
        return e_consumption - e_generation

    def calculate_savings(self, e_generation, e_purchase_price):
        return e_generation * e_purchase_price

    def calculate_payback_time(self, net_cost, yearly_savings):
        return net_cost / yearly_savings

    def calculate(self, acquisition_cost, tax_deduction, e_generation, e_purchase_price):
        net_cost = acquisition_cost - tax_deduction
        yearly_savings = self.calculate_savings(e_generation, e_purchase_price)
        payback_time = self.calculate_payback_time(net_cost, yearly_savings)
        return yearly_savings, payback_time

    def save_calculation(self,
                         user,
                         acquisition_cost,
                         tax_deduction,
                         e_consumption,
                         e_generation,
                         e_purchase_price):
        calculation = Counter(
            acquisition_cost=acquisition_cost,
            tax_deduction=tax_deduction,
            e_consumption=e_consumption,
            e_generation=e_generation,
            e_purchase_price=e_purchase_price,
            user_id=user.id
        )

        yearly_savings, payback_time = self.calculate(
            acquisition_cost,
            tax_deduction,
            e_generation,
            e_purchase_price
        )

        calculation.yearly_savings = yearly_savings
        calculation.payback_time = payback_time

        return self._counter_repository.save_counter(calculation)

    def create_user(self, username, password, login=True):

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Käyttäjätunnus {username} on jo käytössä")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):
        #poista
        print(f"Yritetään kirjautua sisään käyttäjällä: {username}")
        #poista

        user = self._user_repository.find_by_username(username)

        if not user:
            print("Käyttäjää ei löydy.")
            raise InvalidCredentialsError("Virheellinen käyttäjätunnus tai salasana")

        if user.password != password:
            print("Salasana väärin.")
            raise InvalidCredentialsError("Virheellinen käyttäjätunnus tai salasana")

        print(f"Kirjautunut käyttäjä: {user.username}")
        self._user = user

        return user

    def get_user(self):

        return self._user

    def get_users(self):

        return self._user_repository.find_all()

    def logout(self):

        self._user = None

counter_service = CounterService()
