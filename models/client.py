from .person import Person
from interfaces.bonus import Bonus

class Client(Person, Bonus):
    def __init__(self, name, phone, email, birth_date):
        super().__init__(name, phone, email, birth_date)
        self.earned_bonus = 0.0
        self.used_bonus = 0.0
        self.bonus_balance = 0.0

    def add_bonus(self, amount: float):
        self.earned_bonus += amount
        self.bonus_balance += amount

    def use_bonus(self, amount: float) -> float:
        used = min(self.bonus_balance, amount)
        self.bonus_balance -= used
        self.used_bonus += used
        return used
