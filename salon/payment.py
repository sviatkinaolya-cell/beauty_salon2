from interfaces.payable import Payable

class Payment(Payable):
    def pay(self, amount: float, bonus_used: float):
        return amount - bonus_used
