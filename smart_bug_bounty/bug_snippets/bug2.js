// Fetch a user's profile and return the user's display name.
async function getDisplayName(userId) {
  const response = fetch(`/api/users/${userId}`);

  // BUG: response is a Promise because fetch() is not awaited.
  if (!response.ok) {
    throw new Error("Could not load user profile");
  }

  const user = await response.json();

  if (user.displayName) {
    return user.displayName;
  }

  return "Anonymous";
}

getDisplayName(42)
  .then((name) => console.log(name))
  .catch((error) => console.error(error.message));
