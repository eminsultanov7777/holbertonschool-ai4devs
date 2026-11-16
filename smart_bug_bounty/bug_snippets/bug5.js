// Return the total price after applying a percentage discount.
function discountedTotal(prices, discountPercent) {
  if (!Array.isArray(prices)) {
    throw new TypeError("prices must be an array");
  }
  if (discountPercent < 0 || discountPercent > 100) {
    throw new RangeError("discount must be between 0 and 100");
  }

  const subtotal = prices.reduce((total, price) => total + price, 0);

  // BUG: percentage is subtracted as a whole currency amount.
  const total = subtotal - discountPercent;

  if (total < 0) {
    return 0;
  }

  return Math.round(total * 100) / 100;
}

console.log(discountedTotal([50, 50], 10)); // Expected: 90
