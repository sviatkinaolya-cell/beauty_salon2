class BonusCard:
    def __init__(self):
        self.total_earned = 0.0
        self.total_used = 0.0
        self.balance = 0.0

    def add(self, amount):
        self.total_earned += amount
        self.balance += amount

    def use(self, amount):
        used = min(self.balance, amount)
        self.balance -= used
        self.total_used += used
        return used
