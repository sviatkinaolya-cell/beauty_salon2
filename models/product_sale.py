class ProductSale:
    def __init__(self, client, product, quantity, cash_paid, bonus_used):
        self.client = client
        self.product = product
        self.quantity = quantity
        self.cash_paid = cash_paid
        self.bonus_used = bonus_used