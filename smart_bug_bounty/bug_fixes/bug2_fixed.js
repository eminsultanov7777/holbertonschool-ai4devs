// Fetch a user's profile and return their display name.
async function getDisplayName(userId) {
  const response = await fetch(`/api/users/${userId}`);

  if (!response.ok) {
    throw new Error("Could not load user profile");
  }

  const user = await response.json();
  return user.displayName || "Anonymous";
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { getDisplayName };
}
