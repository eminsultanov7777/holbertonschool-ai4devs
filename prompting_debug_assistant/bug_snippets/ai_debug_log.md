# AI Debug Log

This log records the AI-assisted analysis of the five deliberately buggy snippets in `bug_snippets/`.
The same debugging request was used for each sample:

> This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

---

## Bug 1 – bug1.py

**AI Diagnosis**: The `if` statement inside `calculate_average()` is missing a colon after `if len(numbers) == 0`. Python requires a colon to begin an indented block, so the file raises a `SyntaxError` before the function can run.

**Suggested Fix**:
```python
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

values = [10, 20, 30, 40]
print("Average:", calculate_average(values))
```

**Alternative Fixes Tested**: No alternative fix was necessary. The missing colon is the direct syntax issue.

**Result**: After adding the colon, the sample list returns `25.0`. An empty list returns `0`. The syntax issue is resolved.

---

## Bug 2 – bug2.js

**AI Diagnosis**: The condition `age > 18` excludes users who are exactly 18, even though the intended behavior allows registration from age 18 onward. This is a boundary-condition logic error, not a JavaScript syntax error.

**Suggested Fix**:
```javascript
function canRegister(age) {
    return age >= 18;
}
```

**Alternative Fixes Tested**: The original `if` statement can also be kept and changed to `if (age >= 18)`. Both approaches express the same rule.

**Result**: The corrected function returns `false` for ages 16 and 17, and `true` for ages 18, 19, and 25. The boundary case (18) now behaves as intended.

---

## Bug 3 – bug3.py

**AI Diagnosis**: The expression `users[username]` raises a `KeyError` when the requested username is not present in the dictionary. The sample requests `"samir"`, but that key does not exist. The program therefore stops before it can print an email address.

**Suggested Fix**:
```python
def get_email(username):
    email = users.get(username)
    if email is None:
        return None
    return email.lower()

requested_user = "samir"
email = get_email(requested_user)

if email is None:
    print("User not found")
else:
    print("Email:", email)
```

**Alternative Fixes Tested**: Another valid approach is to check `if username not in users` before accessing `users[username]`, or to catch `KeyError` with `try/except`. Using `dict.get()` is concise and avoids the exception for a missing key.

**Result**: For `"samir"`, the corrected code prints `User not found` instead of crashing. For an existing username such as `"aylin"`, it returns and prints the email address in lowercase.

---

## Bug 4 – bug4.c

**AI Diagnosis**: The loop condition `i <= length` allows the loop to access `numbers[length]`. For an array of `length` elements, valid indexes are `0` through `length - 1`. The final iteration therefore reads beyond the array bounds, which is undefined behavior in C.

**Suggested Fix**:
```c
for (int i = 0; i < length; i++)
{
    printf("%d\n", numbers[i]);
}
```

**Alternative Fixes Tested**: The loop could also use a pointer that stops at `numbers + length`, but changing `<=` to `<` is the simplest and clearest correction for this example.

**Result**: With the corrected condition, the program accesses exactly five valid elements and prints `4`, `8`, `12`, `16`, and `20`. The out-of-bounds access is removed. The original program's extra read has undefined behavior, so its output cannot be relied upon.

---

## Bug 5 – bug5.js

**AI Diagnosis**: `toFixed(2)` returns a string, not a number. The expression `total += item.price.toFixed(2)` therefore changes the accumulator from numeric addition to string concatenation. Calling `total.toFixed(2)` afterward may also fail because `total` is then a string.

**Suggested Fix**:
```javascript
function calculateTotal(items) {
    let total = 0;

    for (const item of items) {
        total += item.price;
    }

    return total.toFixed(2);
}

console.log("Cart total:", calculateTotal(cart));
```

**Alternative Fixes Tested**: The code could convert each formatted value back to a number with `Number(item.price.toFixed(2))`, but formatting each item before summing is unnecessary and can introduce rounding differences. Summing numeric values first and formatting once at the end is preferable.

**Result**: The corrected function returns the string `"10.00"` for the sample cart. The total is calculated numerically before formatting, so string concatenation is avoided.

---

## Summary

| Bug | Language | Issue Type | Corrective Action |
|---|---|---|---|
| Bug 1 | Python | Syntax error | Added the missing colon |
| Bug 2 | JavaScript | Logical / boundary error | Changed `>` to `>=` |
| Bug 3 | Python | Runtime exception (`KeyError`) | Handled missing dictionary keys |
| Bug 4 | C | Off-by-one / out-of-bounds access | Changed `<=` to `<` |
| Bug 5 | JavaScript | Data type misuse | Kept the accumulator numeric and formatted at the end |

**Validation note**: The expected outcomes above describe the corrected behavior for the supplied sample inputs. Run each corrected snippet in the local execution environment before submitting if the course requires execution evidence or screenshots.
