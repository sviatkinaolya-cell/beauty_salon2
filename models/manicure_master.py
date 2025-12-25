from .master import Master
import random

class ManicureMaster(Master):
    def provide_service(self):
        services = ["Манікюр", "Педикюр"]
        return random.choice(services)
