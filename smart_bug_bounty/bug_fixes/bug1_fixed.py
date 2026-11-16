def last_items(items, n):
    """Return the last n items from a list."""
    if n < 0:
        raise ValueError("n must not be negative")
    if n == 0:
        return []
    start = max(0, len(items) - n)
    return items[start:]


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]
    print(last_items(values, 3))
