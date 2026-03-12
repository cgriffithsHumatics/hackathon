from app.billing import process_payment


def test_process_payment_success():
    result = process_payment("42", 10)
    assert result["ok"] is True
    assert result["amount"] == 10
