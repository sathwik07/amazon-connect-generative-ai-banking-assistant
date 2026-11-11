from app.services.banking_service import BankingService
from app.services.conversation_service import ConversationService


def test_balance_requires_otp():
    banking = BankingService()
    assistant = ConversationService(banking)

    response = assistant.get_response("balance 1001")

    assert "OTP" in response


def test_balance_after_otp_verification():
    banking = BankingService()
    assistant = ConversationService(banking)

    assistant.get_response("balance 1001")
    otp = assistant.authentication.otp_store["1001"]

    response = assistant.get_response(otp)

    assert "12,500.75" in response


def test_invalid_otp_does_not_show_balance():
    banking = BankingService()
    assistant = ConversationService(banking)

    assistant.get_response("balance 1001")
    response = assistant.get_response("123456")

    assert "Invalid OTP" in response


def test_unknown_account():
    banking = BankingService()
    assistant = ConversationService(banking)

    response = assistant.get_response("balance 9999")

    assert "Account not found" in response
