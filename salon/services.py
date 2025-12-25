from interfaces.payable import Payable
from interfaces.bonus import Bonus
from models.product_sale import ProductSale

class PaymentService:
    """Сервіс для обробки платежів з бонусами"""
    def __init__(self, payment_processor: Payable):
        self.payment_processor = payment_processor

    def process_payment(self, client: Bonus, amount: float, bonus_to_use: float):
        used_bonus = client.use_bonus(bonus_to_use)
        cash_paid = self.payment_processor.pay(amount, used_bonus)
        return cash_paid, used_bonus


class ProductService:
    """Сервіс для продажу продуктів"""
    def sell_product(self, client: Bonus, product, quantity, payment_service: PaymentService):
        total_price = product.price * quantity
        cash_paid, bonus_used = payment_service.process_payment(client, total_price, total_price * 0.1)
        product.quantity -= quantity
        return ProductSale(client, product, quantity, cash_paid, bonus_used)


class ReviewService:
    """Сервіс для додавання відгуків"""
    def add_review(self, salon, client, master, text):
        from models.review import Review
        review = Review(client, master, text)
        salon.add_review(review)
        return review
