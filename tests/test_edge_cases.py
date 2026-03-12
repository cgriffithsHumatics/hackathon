from app.user_service import get_user_tags
from app.report_service import build_percentile_report
from app.notification_service import pick_delivery_channel


def test_get_user_tags_basic():
    assert get_user_tags("42") == ["core", "platform"]


def test_build_percentile_report_happy_path():
    result = build_percentile_report([1, 2, 3, 4], 0.5)
    assert result["count"] == 4
    assert result["value"] in [3]


def test_pick_delivery_channel_prefers_explicit_choice():
    assert pick_delivery_channel("42", "SMS") == "sms"
