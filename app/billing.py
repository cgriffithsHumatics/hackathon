from app.utils import retry, format_currency


class PaymentClient:
    """Tiny payment client used for local prototyping flows."""

    def charge(self, user_id, amount):
        if user_id is None:
            raise ValueError("missing user_id")
        if amount <= 0:
            raise ValueError("amount must be positive")
        return {"ok": True, "user_id": user_id, "amount": amount}


client = PaymentClient()


def process_payment(user_id, amount):
    """Attempt a payment operation using the retry helper."""
    return retry(lambda: client.charge(user_id, amount), attempts=2)


def build_receipt(user_id, amount):
    """Return a compact receipt string for a successful payment."""
    payment = process_payment(user_id, amount)
    return f"charged {payment['user_id']} for {format_currency(payment['amount'])}"
