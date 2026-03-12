from app.user_service import get_user_summary, get_user, search_users


def test_get_user_existing():
    user = get_user("42")
    assert user is not None
    assert user.email == "chris@example.com"


def test_get_user_summary_existing():
    summary = get_user_summary("42")
    assert "Chris Griffiths" in summary
    assert "active" in summary


def test_search_users_basic_match():
    results = search_users("chris")
    assert len(results) == 1
    assert results[0].user_id == "42"
