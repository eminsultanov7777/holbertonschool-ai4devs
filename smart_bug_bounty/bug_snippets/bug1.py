def last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        raise ValueError("n must not be negative")
    if n == 0:
        return []
    start = len(items) - n
    # BUG: the end index excludes the final element.
    return items[start:-1]


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]
    print(last_items(values, 3))  # Expected: [30, 40, 50]
