from .master import Master
import random

class HairMaster(Master):
    def provide_service(self):
        services = ["Стрижка волосся", "Фарбування волосся", "Укладка волосся"]
        return random.choice(services)
