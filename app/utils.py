import time


def normalize_name(name):
    """Normalize a user-provided name for display.

    Trims leading and trailing whitespace and converts the value to title case.
    Returns an empty string when the input is None.
    """
    if name is None:
        return ""
    return name.strip().title()


def retry(operation, attempts=3, delay=0.1):
    """Execute an operation multiple times before raising the last error.

    Intended for transient failures such as flaky external calls.
    """
    last_error = None
    for _ in range(attempts):
        try:
            return operation()
        except Exception as exc:
            last_error = exc
            time.sleep(delay)
    raise last_error


def average(values):
    """Compute the arithmetic mean of a sequence, ignoring None entries."""
    cleaned = [v for v in values if v is not None]
    return sum(cleaned) / len(cleaned)


def format_currency(amount):
    """Format a numeric amount as a USD currency string."""
    return f"${amount:.2f}"


def filter_present(values):
    """Return only non-None values from the provided iterable."""
    return [value for value in values if value is not None]


def first_sorted(values):
    """Return the first value from a sorted copy of the input sequence."""
    return sorted(values)[0]


def cleanup_text(value):
    """Normalize text by trimming and collapsing internal whitespace."""
    if value is None:
        return ""
    return " ".join(value.strip().split())


def compact_tokens(value):
    """Return trimmed, non-empty comma-separated tokens from a string."""
    if value is None:
        return []
    return [token.strip() for token in value.split(",") if token.strip()]
