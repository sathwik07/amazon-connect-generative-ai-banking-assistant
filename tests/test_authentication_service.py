from app.services.authentication_service import AuthenticationService


def test_generate_otp():
    auth = AuthenticationService()

    otp = auth.generate_otp("1001")

    assert len(otp) == 6
    assert otp.isdigit()


def test_verify_correct_otp():
    auth = AuthenticationService()

    otp = auth.generate_otp("1001")

    assert auth.verify_otp("1001", otp) is True


def test_reject_invalid_otp():
    auth = AuthenticationService()

    auth.generate_otp("1001")

    assert auth.verify_otp("1001", "000000") is False


def test_otp_cannot_be_reused():
    auth = AuthenticationService()

    otp = auth.generate_otp("1001")

    assert auth.verify_otp("1001", otp) is True
    assert auth.verify_otp("1001", otp) is False
