from app.api import get_user_report


def test_get_user_report_happy_path():
    result = get_user_report("42", [1, 2, 3])
    assert "Chris Griffiths" in result["user"]
    assert result["metrics"]["average"] == 2
