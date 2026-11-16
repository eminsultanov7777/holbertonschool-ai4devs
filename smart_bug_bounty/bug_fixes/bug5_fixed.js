// Return the total price after applying a percentage discount.
function discountedTotal(prices, discountPercent) {
  if (!Array.isArray(prices)) {
    throw new TypeError("prices must be an array");
  }

  if (
    typeof discountPercent !== "number" ||
    discountPercent < 0 ||
    discountPercent > 100
  ) {
    throw new RangeError("discount must be a number between 0 and 100");
  }

  const subtotal = prices.reduce((total, price) => total + price, 0);
  const total = subtotal * (1 - discountPercent / 100);

  if (total < 0) {
    return 0;
  }

  return Math.round(total * 100) / 100;
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { discountedTotal };
}
