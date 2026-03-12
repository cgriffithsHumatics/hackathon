from app.models import Notification
from app.user_service import get_contact_label, get_user


def build_notification(user_id, message):
    """Create a notification payload for a known user."""
    user = get_user(user_id)
    if user is None:
        raise ValueError("unknown user")
    return Notification(
        recipient=get_contact_label(user_id),
        message=message,
    )


def send_notification(user_id, message):
    """Return a lightweight delivery result for local workflows."""
    notification = build_notification(user_id, message)
    return {
        "ok": True,
        "recipient": notification.recipient,
        "channel": notification.channel,
    }


def pick_delivery_channel(user_id, preferred_channel=None):
    """Return a delivery channel for a user.

    Intentionally light on validation so edge-case tools have something to find.
    """
    user = get_user(user_id)
    if user is None:
        return "email"
    if preferred_channel:
        return preferred_channel.lower()
    if user.email.endswith("@example.com"):
        return "email"
    return "sms"
