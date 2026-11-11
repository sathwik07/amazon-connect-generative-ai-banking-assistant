from app.services.bedrock_service import BedrockService
from app.services.knowledge_base import get_knowledge_base


class ConversationService:
    def __init__(self, banking_service):
        self.banking_service = banking_service
        self.pending_intent = None
        self.bedrock = BedrockService(get_knowledge_base())

    def get_response(self, message):
        message = message.lower().strip()

        if self.pending_intent:
            if not message.isdigit() or len(message) != 4:
                return "Please enter a valid 4-digit demo account number."

            intent = self.pending_intent
            self.pending_intent = None
            return self._process_request(intent, message)

        if any(word in message for word in ["balance", "amount"]):
            intent = "balance"
        elif any(word in message for word in ["transaction", "payment"]):
            intent = "transactions"
        elif any(word in message for word in ["account", "customer"]):
            intent = "account"
        else:
            return self.bedrock.generate_response(message)

        account_number = next(
            (word for word in message.split()
             if word.isdigit() and len(word) == 4),
            None
        )

        if not account_number:
            self.pending_intent = intent
            return "Please enter your 4-digit demo account number."

        return self._process_request(intent, account_number)

    def _process_request(self, intent, account_number):
        account = self.banking_service.get_account(account_number)

        if not account:
            return "Account not found. Please check the account number."

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

            return "Recent transactions:\n" + "\n".join(details)

        return (
            f"Account holder: {account['name']}\n"
            f"Account type: {account['account_type']}\n"
            f"Account number: {account['account_number']}"
        )
