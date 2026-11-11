class LexService:
    def __init__(self):
        self.intents = {
            "CheckBalance": ["balance", "available balance"],
            "TransactionHistory": ["transactions", "recent payments"],
            "AccountDetails": ["account details", "account information"],
            "CardSupport": ["lost card", "blocked card"]
        }

    def detect_intent(self, message):
        message = message.lower().strip()

        for intent, keywords in self.intents.items():
            if any(keyword in message for keyword in keywords):
                return {
                    "intent": intent,
                    "message": message
                }

        return {
            "intent": "FallbackIntent",
            "message": message
        }
