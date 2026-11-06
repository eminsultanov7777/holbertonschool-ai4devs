# Fixed Bug 3: Handle missing dictionary keys safely.

users = {
    "aylin": "aylin@example.com",
    "murad": "murad@example.com",
    "leyla": "leyla@example.com"
}

def get_email(username):
    email = users.get(username)
    if email is None:
        return None
    return email.lower()

assert get_email("aylin") == "aylin@example.com"
assert get_email("samir") is None
print("Bug 3 tests passed")
