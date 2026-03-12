from app.utils import normalize_name, average


def test_normalize_name():
    assert normalize_name("  hello world ") == "Hello World"


def test_average_ignores_none_values():
    assert average([1, None, 3]) == 2
