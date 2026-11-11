class ConnectService:
    def __init__(self, conversation_service):
        self.conversation_service = conversation_service

    def handle_contact(self, event):
        customer_input = event.get("Details", {}).get(
            "Parameters", {}
        ).get("customer_input", "")

        if not customer_input:
            return {
                "status": "error",
                "message": "No customer input received."
            }

        response = self.conversation_service.get_response(
            customer_input
        )

        return {
            "status": "success",
            "response": response
        }

    def handle_chat_message(self, message):
        response = self.conversation_service.get_response(message)

        return {
            "channel": "chat",
            "response": response
        }
