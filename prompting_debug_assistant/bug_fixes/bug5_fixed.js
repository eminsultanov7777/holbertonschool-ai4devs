// Fixed Bug 5: Keep the accumulator numeric and format once at the end.

const cart = [
    { name: "Notebook", price: 5 },
    { name: "Pen", price: 2 },
    { name: "Folder", price: 3 }
];

function calculateTotal(items) {
    let total = 0;

    for (const item of items) {
        total += item.price;
    }

    return total.toFixed(2);
}

if (calculateTotal(cart) !== "10.00") throw new Error("Cart total should be 10.00");
if (calculateTotal([]) !== "0.00") throw new Error("Empty cart total should be 0.00");

console.log("Bug 5 tests passed");
