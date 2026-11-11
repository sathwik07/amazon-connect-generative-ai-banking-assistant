from app.services.banking_service import BankingService


def test_get_account():
    banking = BankingService()
    account = banking.get_account("1001")

    assert account is not None
    assert account["name"] == "John Smith"


def test_get_balance():
    banking = BankingService()

    assert banking.get_balance("1001") == 12500.75


def test_invalid_account():
    banking = BankingService()

    assert banking.get_account("9999") is None


def test_recent_transactions():
    banking = BankingService()
    transactions = banking.get_recent_transactions("1001")

    assert len(transactions) == 3
    assert transactions[0]["description"] == "Grocery Store"
