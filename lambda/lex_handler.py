def lambda_handler(event, context):
    from app.services.lex_service import LexService

    lex = LexService()

    user_message = event.get("inputTranscript", "")

    if not user_message:
        return {
            "sessionState": {
                "dialogAction": {"type": "ElicitIntent"}
            },
            "messages": [
                {"contentType": "PlainText",
                 "content": "How can I help you today?"}
            ]
        }

    result = lex.detect_intent(user_message)

    return {
        "sessionState": {
            "dialogAction": {"type": "Close"},
            "intent": {
                "name": result["intent"],
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "Your request was received."
            }
        ]
    }
