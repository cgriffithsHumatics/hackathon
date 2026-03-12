from app.user_service import get_user_summary
from app.report_service import build_daily_report, build_clean_report
from app.search_tools import recommend_contacts
from app.workflows import build_onboarding_packet
from app.analytics import build_dashboard_data


def get_user_report(user_id, values):
    """Return a simple user-plus-metrics response payload."""
    return {
        "user": get_user_summary(user_id),
        "metrics": build_daily_report(values),
    }


def get_clean_user_report(user_id, values):
    """Return a user report that tolerates sparse metric values."""
    return {
        "user": get_user_summary(user_id),
        "metrics": build_clean_report(values),
    }


def suggest_contacts(task_text):
    """Return likely contact suggestions for the provided task text."""
    return {
        "matches": recommend_contacts(task_text),
    }


def get_onboarding_preview(user_id, values, amount):
    """Return a combined onboarding preview payload."""
    return build_onboarding_packet(user_id, values, amount)


def get_dashboard_preview(user_ids, values):
    """Return a lightweight analytics preview payload."""
    return {
        "dashboard": build_dashboard_data(user_ids, values),
    }
