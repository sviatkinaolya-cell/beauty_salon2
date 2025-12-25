import random
from datetime import date

from models.client import Client
from models.manicure_master import ManicureMaster
from models.hair_master import HairMaster
from models.product import Product
from salon.appointment import Appointment
from salon.beauty_salon import BeautySalon
from salon.payment import Payment
from salon.services import PaymentService, ProductService, ReviewService

# ===== Створення салону та сервісів =====
payment_processor = Payment()
payment_service = PaymentService(payment_processor)
product_service = ProductService()
review_service = ReviewService()

salon = BeautySalon("Luxury Beauty")

# ===== Майстри =====
masters = [
    ManicureMaster("Анна", "+380981111111", "anna@gmail.com", date(1998,3,20), 5, 500),
    ManicureMaster("Ірина", "+380982222222", "iryna@gmail.com", date(1997,6,11), 6, 600),
    HairMaster("Оксана", "+380983333333", "oksana@gmail.com", date(1995,1,5), 9, 700),
    HairMaster("Марія", "+380984444444", "maria@gmail.com", date(1999,9,14), 4, 1200),
]

# ===== Клієнти =====
clients = [
    Client("Оля", "+380991111111", "olya@gmail.com", date(2004,5,12)),
    Client("Юля", "+380992222222", "yulia@gmail.com", date(2003,8,22)),
    Client("Катя", "+380993333333", "katya@gmail.com", date(2002,11,2)),
    Client("Аня", "+380994444444", "anya@gmail.com", date(2001,4,17)),
    Client("Інна", "+380995555555", "inna@gmail.com", date(2000,6,30)),
    Client("Марина", "+380996666666", "marina@gmail.com", date(2005,2,9)),
]

# ===== Додаємо майстрів і клієнтів =====
for m in masters:
    salon.add_master(m)
for c in clients:
    salon.add_client(c)

# ===== Продукти =====
products = [
    Product("Шампунь", 200, 10),
    Product("Лак для нігтів", 150, 5),
    Product("Маска для волосся", 250, 7),
]
for p in products:
    salon.add_product(p)

# ===== Імітація роботи салону =====
for client in salon.clients:
    master = random.choice(salon.masters)
    service_name = master.provide_service()
    appointment = Appointment(client, master, date.today())

    # Нарахування бонусів
    client.add_bonus(master.service_price * 0.05)

    # Оплата послуги
    cash_paid, used_bonus = payment_service.process_payment(client, master.service_price, master.service_price * 0.3)
    salon.create_appointment(appointment, cash_paid, used_bonus)

    # Відгук
    review_text = f"Послуга '{service_name}' сподобалась!"
    review_service.add_review(salon, client, master, review_text)

    # Продаж продукту
    product = random.choice(salon.products)
    if product.quantity > 0:
        quantity = random.randint(1, min(2, product.quantity))
        sale = product_service.sell_product(client, product, quantity, payment_service)
        salon.add_product_sale(sale)

# ===== Звіт =====
print("\n========== ПОВНИЙ ЗВІТ САЛОНУ ==========\n")
for a in salon.appointments:
    print(f"Клієнт: {a.client.name} | Майстер: {a.master.name} | Послуга: {a.master.provide_service()} | Ціна: {a.master.service_price} грн")

print("\n========== БОНУСИ КЛІЄНТІВ ==========")
for c in salon.clients:
    print(f"{c.name} | Нараховано: {round(c.earned_bonus,2)} грн | Списано: {round(c.used_bonus,2)} грн | Залишок: {round(c.bonus_balance,2)} грн")

print("\n========== ПРОДУКТИ (КОМУ ПРОДАНО) ==========")
for sale in salon.product_sales:
    print(f"{sale.client.name} купив {sale.quantity} шт. {sale.product.name} | Оплата готівкою: {round(sale.cash_paid,2)} грн | Бонусом: {round(sale.bonus_used,2)} грн")

print("\n========== ЗАЛИШОК ПРОДУКТІВ ==========")
for p in salon.products:
    print(f"{p.name}: залишок {p.quantity} шт.")

print("\n========== ВІДГУКИ ==========")
for r in salon.reviews:
    print(f"{r.client.name} про {r.master.name}: {r.text}")

print("\n========== ФІНАНСИ САЛОНУ ==========")
print(f"Оплачено грошима: {round(salon.income_cash,2)} грн")
print(f"Оплачено бонусами: {round(salon.income_bonus,2)} грн")
print(f"Загальний оборот: {round(salon.income_cash + salon.income_bonus,2)} грн")
print("\n========== КІНЕЦЬ ПРОГРАМИ ==========")
