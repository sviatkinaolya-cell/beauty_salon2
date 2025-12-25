class PhoneValidator:
    @staticmethod
    def validate(phone: str):
        return phone.startswith("+380")

