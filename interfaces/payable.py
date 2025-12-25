from abc import ABC, abstractmethod

class Payable(ABC):
    @abstractmethod
    def pay(self, amount: float, bonus_used: float):
        pass
