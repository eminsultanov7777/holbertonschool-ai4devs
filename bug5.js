// Bug 5: Misuse of data types
// Intended behavior: Calculate the total price of all items in the cart.

const cart = [
    { name: "Notebook", price: 5 },
    { name: "Pen", price: 2 },
    { name: "Folder", price: 3 }
];

function calculateTotal(items) {
    let total = 0;

    for (const item of items) {
        total += item.price.toFixed(2);
    }

    return total.toFixed(2);
}

console.log("Cart total:", calculateTotal(cart));

// toFixed() returns a string, so total becomes a string after the first item.
