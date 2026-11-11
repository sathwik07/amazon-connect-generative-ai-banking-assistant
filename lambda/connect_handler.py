def lambda_handler(event, context):
    from app.services.banking_service import BankingService
    from app.services.conversation_service import ConversationService
    from app.services.connect_service import ConnectService

    banking = BankingService()
    assistant = ConversationService(banking)
    connect = ConnectService(assistant)

    return connect.handle_contact(event)
