"""python_basics.py — Day 1: functions, comprehensions, type hints, error handling."""


def parse_average(values: list[str]) -> float:
    """Convert a list of strings to numbers and return their average."""
    if not values:
        raise ValueError("Got an empty list — nothing to average.")
    try:
        numbers = [float(v) for v in values]
    except ValueError as err:
        raise ValueError(f"Couldn't parse {values!r} as numbers: {err}") from err
    return sum(numbers) / len(numbers)


def filter_words(words: list[str], min_length: int) -> list[str]:
    """Lowercase and strip each word, keeping only those longer than min_length."""
    if not words:
        raise ValueError("Got an empty list — nothing to filter.")
    if min_length < 0:
        raise ValueError(f"min_length must be >= 0, got {min_length}.")
    return [w.strip().lower() for w in words if len(w.strip()) > min_length]


def safe_divide_all(numbers: list[float], divisor: float) -> list[float]:
    """Divide every number in a list by divisor."""
    if divisor == 0:
        raise ValueError("Division by 0 is not possible.")
    return [n / divisor for n in numbers]


if __name__ == "__main__":
    print(parse_average(["10", "20", "30"]))
    print(filter_words(["  Cat", "Elephant ", "Dog"], 3))
    print(safe_divide_all([10, 20, 30], 2))