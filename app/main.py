from app.user_service import get_user_summary
from app.report_service import build_daily_report, build_metric_overview
from app.api import get_user_report, suggest_contacts
from app.workflows import build_onboarding_packet, process_user_lifecycle
from app.legacy_helpers import buildThing
from app.analytics import build_dashboard_data


def run():
    print(get_user_summary("42"))
    print(build_daily_report([1, 2, 2, 3, None]))
    print(get_user_report("42", [10, 15, 20]))
    print(suggest_contacts("please follow up with alex about the daily report"))
    print(build_onboarding_packet("44", [3, 4, 5], 19.99))
    print(build_metric_overview(" Daily Report Latency ", [2, None, 6, 8]))
    print(process_user_lifecycle("44", [3, 4, 5], 19.99, send_welcome=False))
    print(buildThing([" a ", None, "b"], flag=True, mode="reverse"))
    print(build_dashboard_data(["42", "44"], [1, 2, 3, 4]))


if __name__ == "__main__":
    run()
