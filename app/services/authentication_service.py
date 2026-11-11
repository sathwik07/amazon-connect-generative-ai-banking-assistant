import random


class AuthenticationService:
    def __init__(self):
        self.otp_store = {}

    def generate_otp(self, account_number):
        otp = str(random.randint(100000, 999999))
        self.otp_store[str(account_number)] = otp
        return otp

    def verify_otp(self, account_number, entered_otp):
        account_number = str(account_number)
        stored_otp = self.otp_store.get(account_number)

        if not stored_otp:
            return False

        if stored_otp == str(entered_otp):
            del self.otp_store[account_number]
            return True

        return False
