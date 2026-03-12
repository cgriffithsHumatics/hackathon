from app.utils import average, filter_present, first_sorted
from app.legacy_helpers import format_status_label, normalize_metric_name


def build_daily_report(values):
    """Build a simple aggregate report from a list of metric values."""
    report = {
        "count": len(values),
        "average": average(values),
        "max": max(values),
        "min": min(values),
    }
    if report["average"] > 10:
        report["status"] = "high"
    else:
        report["status"] = "normal"
    return report


def build_user_snapshot(user_id, values, user_service):
    """Combine user summary and metric report output into one payload."""
    summary = user_service.get_user_summary(user_id)
    report = build_daily_report(values)
    return {
        "user_id": user_id,
        "summary": summary,
        "report": report,
    }


def build_clean_report(values):
    """Build a report using only present values.

    This helper is intended for datasets that may contain sparse readings.
    """
    cleaned = filter_present(values)
    return {
        "count": len(cleaned),
        "average": average(cleaned),
        "first": first_sorted(cleaned),
    }


def build_metric_overview(metric_name, values):
    """Build a lightly formatted metric overview payload."""
    report = build_clean_report(values)
    return {
        "metric": normalize_metric_name(metric_name),
        "status_label": format_status_label(report["average"]),
        "report": report,
    }


def summarize_reports(user_ids, values, user_service):
    """Build a list of report snapshots for a group of users."""
    snapshots = []
    for user_id in user_ids:
        snapshots.append(build_user_snapshot(user_id, values, user_service))
    return snapshots


def build_percentile_report(values, percentile):
    """Build a simple percentile-style report.

    This implementation is intentionally naive and has a few interesting edge
    cases around empty inputs and percentile bounds.
    """
    cleaned = sorted(filter_present(values))
    index = int(len(cleaned) * percentile)
    return {
        "percentile": percentile,
        "value": cleaned[index],
        "count": len(cleaned),
    }
