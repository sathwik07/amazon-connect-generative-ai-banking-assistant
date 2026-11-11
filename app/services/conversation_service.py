
class ConversationService:
    def __init__(self, banking_service):
        self.banking_service = banking_service
        self.pending_intent = None

    def get_response(self, message):
        message = message.lower().strip()

        if self.pending_intent:
            account_number = message

            if not account_number.isdigit() or len(account_number) != 4:
                return "Please enter a valid 4-digit account number."

            intent = self.pending_intent
            self.pending_intent = None

            return self._process_request(intent, account_number)

        if any(word in message for word in ["balance", "amount", "money"]):
            intent = "balance"

        elif any(word in message for word in ["transaction", "transactions", "payment"]):
            intent = "transactions"

        elif any(word in message for word in ["account", "customer"]):
            intent = "account"

        else:
            return (
                "I can help with account details, balance inquiries, "
                "and recent transactions. What would you like to know?"
            )

        account_number = next(
            (word for word in message.split() if word.isdigit() and len(word) == 4),
            None
        )

        if not account_number:
            self.pending_intent = intent
            return "Please enter your 4-digit demo account number."

        return self._process_request(intent, account_number)

    def _process_request(self, intent, account_number):
        account = self.banking_service.get_account(account_number)

        if not account:
            return "I couldn't find an account with that number."

        if intent == "balance":
            balance = self.banking_service.get_balance(account_number)
            return f"Your available balance is ${balance:,.2f}."

        if intent == "transactions":
            transactions = self.banking_service.get_recent_transactions(
                account_number
            )

            if not transactions:
                return "No recent transactions were found."

            details = [
                f"{item['date']} - {item['description']}: "
                f"${item['amount']:,.2f}"
                for item in transactions
            ]

            return "Here are your recent transactions:\n" + "\n".join(details)

        return (
            f"Account holder: {account['name']}\n"
            f"Account type: {account['account_type']}\n"
            f"Account number: {account['account_number']}"
        )
