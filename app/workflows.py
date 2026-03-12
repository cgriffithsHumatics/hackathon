from app.billing import build_receipt
from app.notification_service import send_notification
from app.report_service import build_user_snapshot
from app.user_service import get_user_summary
import app.user_service as user_service


def build_onboarding_packet(user_id, values, amount):
    """Assemble a multi-step onboarding payload for a user."""
    summary = get_user_summary(user_id)
    snapshot = build_user_snapshot(user_id, values, user_service)
    receipt = build_receipt(user_id, amount)
    delivery = send_notification(user_id, f"Welcome: {summary}")
    return {
        "summary": summary,
        "snapshot": snapshot,
        "receipt": receipt,
        "delivery": delivery,
    }


def process_user_lifecycle(user_id, values, amount, send_welcome=True, include_report=True, include_payment=True):
    """Legacy orchestration helper with several branching paths.

    This function intentionally mixes validation, transformation, control flow,
    and response formatting to create refactoring opportunities.
    """
    result = {}
    if user_id is None or user_id == "":
        result["status"] = "error"
        result["message"] = "missing user"
    else:
        summary = get_user_summary(user_id)
        result["summary"] = summary
        if "not found" in summary:
            result["status"] = "error"
            result["message"] = "unknown user"
        else:
            result["status"] = "ok"
            if include_report:
                if values is None:
                    result["report"] = {"error": "missing values"}
                else:
                    if len(values) == 0:
                        result["report"] = {"count": 0, "status": "empty"}
                    else:
                        cleaned = []
                        for value in values:
                            if value is not None:
                                cleaned.append(value)
                        if len(cleaned) == 0:
                            result["report"] = {"count": 0, "status": "empty"}
                        else:
                            snapshot = build_user_snapshot(user_id, cleaned, user_service)
                            result["report"] = snapshot["report"]
            if include_payment:
                if amount is None:
                    result["receipt"] = "payment skipped"
                else:
                    if amount > 0:
                        result["receipt"] = build_receipt(user_id, amount)
                    else:
                        result["receipt"] = "invalid payment"
            if send_welcome:
                delivery = send_notification(user_id, f"Welcome: {summary}")
                result["delivery"] = delivery
            else:
                result["delivery"] = {"ok": False, "reason": "disabled"}
    if result.get("status") == "ok":
        if include_report and include_payment and send_welcome:
            result["mode"] = "full"
        elif include_report and include_payment:
            result["mode"] = "partial-no-welcome"
        elif include_report:
            result["mode"] = "report-only"
        else:
            result["mode"] = "summary-only"
    else:
        result["mode"] = "error"
    return result


def build_team_digest(user_ids, values, amount):
    """Build a digest payload for a list of users.

    Intentionally performs repeated per-user work so performance tools have
    something meaningful to detect.
    """
    digest = []
    for user_id in user_ids:
        digest.append(build_onboarding_packet(user_id, values, amount))
    return {
        "count": len(digest),
        "items": digest,
    }
