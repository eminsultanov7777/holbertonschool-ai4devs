def add_tag(tag, tags=None):
    """Return a list containing the supplied tag without shared default state."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def build_labels(items):
    labels = []
    for item in items:
        labels = add_tag(item, labels)
    return labels


if __name__ == "__main__":
    print(add_tag("urgent"))
    print(add_tag("review"))
