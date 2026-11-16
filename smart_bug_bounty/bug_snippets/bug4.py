def add_tag(tag, tags=[]):
    """Return a new list containing the supplied tag."""
    # BUG: the default list is shared between function calls.
    tags.append(tag)
    return tags


def build_labels(items):
    labels = []
    for item in items:
        labels = add_tag(item, labels)
    return labels


if __name__ == "__main__":
    print(add_tag("urgent"))  # Expected: ["urgent"]
    print(add_tag("review"))  # Expected: ["review"], but old tag remains
