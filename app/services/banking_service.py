
class BankingService:
    def __init__(self):
        self.customers = {
            "1001": {
                "name": "John Smith",
                "account_number": "1001",
                "balance": 12500.75,
                "account_type": "Savings",
                "currency": "USD"
            },
            "1002": {
                "name": "Emily Johnson",
                "account_number": "1002",
                "balance": 8750.50,
                "account_type": "Checking",
                "currency": "USD"
            }
        }

        self.transactions = {
            "1001": [
                {"date": "2026-11-08", "description": "Grocery Store", "amount": -85.50},
                {"date": "2026-11-06", "description": "Salary Deposit", "amount": 3500.00},
                {"date": "2026-11-04", "description": "Utility Bill", "amount": -120.00}
            ],
            "1002": [
                {"date": "2026-11-09", "description": "Online Purchase", "amount": -65.00},
                {"date": "2026-11-07", "description": "Monthly Deposit", "amount": 1500.00}
            ]
        }

    def get_account(self, account_number):
        return self.customers.get(str(account_number))

    def get_balance(self, account_number):
        account = self.get_account(account_number)

        if not account:
            return None

        return account["balance"]

    def get_recent_transactions(self, account_number, limit=5):
        account_number = str(account_number)

        if account_number not in self.customers:
            return None

        return self.transactions.get(account_number, [])[:limit]
