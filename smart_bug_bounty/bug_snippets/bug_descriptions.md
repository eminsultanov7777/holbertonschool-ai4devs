# Bug Descriptions

This collection contains five intentionally flawed snippets in Python, JavaScript, and Java. Each snippet is designed for debugging practice. The descriptions state the intended behavior and the known defect without providing a corrected implementation.

## bug1.py

- **Language:** Python
- **Intended Behavior:** Return the last `n` items from a list. For example, `last_items([10, 20, 30, 40, 50], 3)` should return `[30, 40, 50]`.
- **Current Issue:** The slice uses `-1` as its end index, which excludes the final list element. The returned list is therefore missing an item.

## bug2.js

- **Language:** JavaScript
- **Intended Behavior:** Fetch a user's profile from an API, check the HTTP response, parse the JSON body, and return the user's display name or `"Anonymous"` when no display name is present.
- **Current Issue:** The `fetch()` call is not awaited. The code attempts to read `ok` from a Promise instead of from the resolved Response object.

## bug3.java

- **Language:** Java
- **Intended Behavior:** Calculate and return the arithmetic mean of an integer array as a `double`. For `{80, 81}`, the result should be `80.5`.
- **Current Issue:** Both operands in the division are integers, so Java performs integer division before converting the result to `double`. The fractional part is lost.

## bug4.py

- **Language:** Python
- **Intended Behavior:** Add a tag to a list and return the resulting list. Separate calls that omit the optional `tags` argument should start with independent empty lists.
- **Current Issue:** The function uses a mutable list as a default argument. Python creates that list once, so values from earlier calls remain in later results.

## bug5.js

- **Language:** JavaScript
- **Intended Behavior:** Calculate the subtotal of a list of prices, apply a percentage discount, and return the discounted total rounded to two decimal places. For prices `[50, 50]` and a 10% discount, the result should be `90`.
- **Current Issue:** The code subtracts the discount percentage as a fixed currency amount instead of calculating that percentage of the subtotal.

## Summary

| File | Language | Bug Category |
|---|---|---|
| `bug1.py` | Python | Off-by-one slicing error |
| `bug2.js` | JavaScript | Missing `await` / Promise handling |
| `bug3.java` | Java | Integer division precision |
| `bug4.py` | Python | Mutable default argument |
| `bug5.js` | JavaScript | Incorrect percentage calculation |
