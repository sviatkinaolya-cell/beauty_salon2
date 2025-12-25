class EmailValidator:
    @staticmethod
    def validate(email: str):
        return "@" in email
