from abc import ABC, abstractmethod

class Bonus(ABC):
    @abstractmethod
    def add_bonus(self, amount: float):
        pass
