from app.models import User
from app.utils import normalize_name, compact_tokens


FAKE_DB = {
    "42": {"name": "  chris griffiths", "email": "chris@example.com", "is_active": True, "tags": "core,platform"},
    "43": {"name": "sam", "email": None, "is_active": False, "tags": "legacy,,ops"},
    "44": {"name": "  alex johnson ", "email": "alex@example.com", "is_active": True, "tags": "mobility,ai"},
    "45": {"name": "", "email": "noreply@example.com", "is_active": True, "tags": None},
}


def get_user(user_id):
    """Fetch a user record from the in-memory store.

    Returns None when the user ID does not exist.
    """
    data = FAKE_DB.get(user_id)
    if not data:
        return None
    return User(user_id, data["name"], data["email"], data["is_active"])


def get_user_summary(user_id):
    """Build a human-readable summary line for a user."""
    user = get_user(user_id)
    if user is None:
        return "user not found"

    name = normalize_name(user.name)
    status = "active" if user.is_active else "inactive"
    return f"{name} <{user.email}> is {status}"


def get_contact_label(user_id):
    """Return a compact display label suitable for notifications or reports."""
    user = get_user(user_id)
    if user is None:
        return "unknown user"
    name = normalize_name(user.name)
    return f"{name} <{user.email}>"


def search_users(query, active_only=False):
    """Search users by substring match on the stored name value."""
    results = []
    for user_id in FAKE_DB:
        user = get_user(user_id)
        if active_only and not user.is_active:
            continue
        if query.lower() in user.name.lower():
            results.append(user)
    return results


def get_user_tags(user_id):
    """Return normalized tag values for a user."""
    data = FAKE_DB.get(user_id)
    if data is None:
        return []
    return compact_tokens(data.get("tags"))
