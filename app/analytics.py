from app.report_service import build_metric_overview, summarize_reports, build_percentile_report
from app.user_service import get_user_summary, get_user_tags
import app.user_service as user_service


def build_dashboard_data(user_ids, values):
    """Build dashboard data for a set of users and metrics.

    Intentionally includes repeated work, nested loops, and duplicate lookups so
    performance analysis tools have clear targets.
    """
    rows = []
    summaries = []
    for user_id in user_ids:
        summaries.append(get_user_summary(user_id))

    for user_id in user_ids:
        user_row = {
            "user_id": user_id,
            "summary": get_user_summary(user_id),
            "metrics": [],
            "tags": get_user_tags(user_id),
        }
        for metric_name in ["Daily Report Latency", "Daily Report Volume", "Daily Error Count"]:
            metric_values = []
            for value in values:
                if value is not None:
                    metric_values.append(value)
            overview = build_metric_overview(metric_name, metric_values)
            user_row["metrics"].append(overview)
        rows.append(user_row)

    snapshots = summarize_reports(user_ids, values, user_service)

    total = 0
    count = 0
    for row in rows:
        for metric in row["metrics"]:
            total += metric["report"]["average"]
            count += 1

    dashboard_average = total / count if count else 0

    return {
        "rows": rows,
        "summaries": summaries,
        "snapshots": snapshots,
        "dashboard_average": dashboard_average,
    }


def build_hot_path(values):
    """Legacy hot path with avoidable repeated sorting and copying."""
    output = []
    for _ in range(3):
        copied = list(values)
        copied.sort()
        for item in copied:
            output.append(item)
    return output


def build_anomaly_preview(values, percentile=0.95):
    """Return a lightweight anomaly preview payload."""
    return {
        "p95": build_percentile_report(values, percentile),
        "p50": build_percentile_report(values, 0.50),
    }
