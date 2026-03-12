from app.user_service import search_users, get_contact_label
from app.utils import normalize_name


def recommend_contacts(task_text):
    """Suggest likely matching contacts for a free-form task description.

    The function looks for mentions of known user names and returns lightweight
    contact labels for possible matches.
    """
    normalized = normalize_name(task_text)
    matches = []
    for token in normalized.split():
        users = search_users(token)
        for user in users:
            label = get_contact_label(user.user_id)
            if label not in matches:
                matches.append(label)
    return matches
