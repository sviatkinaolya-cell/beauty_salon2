class BeautySalon:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.masters = []
        self.appointments = []
        self.products = []
        self.reviews = []
        self.product_sales = []
        self.income_cash = 0.0
        self.income_bonus = 0.0

    def add_client(self, client):
        self.clients.append(client)

    def add_master(self, master):
        self.masters.append(master)

    def create_appointment(self, appointment, cash_paid, bonus_used):
        self.appointments.append(appointment)
        self.income_cash += cash_paid
        self.income_bonus += bonus_used

    def add_product(self, product):
        self.products.append(product)

    def add_review(self, review):
        self.reviews.append(review)

    def add_product_sale(self, sale):
        self.product_sales.append(sale)
