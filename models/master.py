from .person import Person
from interfaces.serviceable import Serviceable

class Master(Person, Serviceable):
    def __init__(self, name, phone, email, birth_date, experience, service_price):
        super().__init__(name, phone, email, birth_date)
        self.experience = experience
        self.service_price = service_price

    def provide_service(self) -> str:
        return "Надає послугу"

