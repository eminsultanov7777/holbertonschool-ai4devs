# Bug 3: Runtime exception
# Intended behavior: Find a user's email by username.

users = {
    "aylin": "aylin@example.com",
    "murad": "murad@example.com",
    "leyla": "leyla@example.com"
}

def get_email(username):
    email = users[username]
    return email.lower()

requested_user = "samir"
print("Email:", get_email(requested_user))

# The program crashes when the username is not in the dictionary.
