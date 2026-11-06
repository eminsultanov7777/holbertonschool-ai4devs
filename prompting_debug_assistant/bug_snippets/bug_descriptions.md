# Bug Descriptions

This document describes the intended behavior of each deliberately flawed code sample in `bug_snippets/`.

## Bug 1 – bug1.py
**Intended Behavior**: Calculate and return the arithmetic average of a list of numbers. If the list is empty, return `0`.

**Issue Type**: Syntax error.

**Notes**: The `if` statement is missing a colon, so Python cannot parse the function. The intended calculation should work after the syntax is corrected.

## Bug 2 – bug2.js
**Intended Behavior**: Return `true` when a user's age is 18 or older, and `false` otherwise.

**Issue Type**: Logical error.

**Notes**: The condition uses `age > 18`, which incorrectly rejects users who are exactly 18. The boundary condition should include 18.

## Bug 3 – bug3.py
**Intended Behavior**: Return the email address for a username. If the username does not exist, handle the missing user gracefully instead of crashing.

**Issue Type**: Runtime exception.

**Notes**: Accessing `users[username]` raises a `KeyError` when the requested username is absent. The sample requests `samir`, who is not in the dictionary.

## Bug 4 – bug4.c
**Intended Behavior**: Print each element of the five-element array exactly once.

**Issue Type**: Off-by-one / loop boundary error.

**Notes**: The loop condition uses `i <= length`. Valid array indexes range from `0` through `length - 1`, so the final iteration accesses memory beyond the array.

## Bug 5 – bug5.js
**Intended Behavior**: Add the numeric prices of all cart items and return the total formatted to two decimal places.

**Issue Type**: Misuse of data types / library method.

**Notes**: `toFixed(2)` returns a string. Adding that string to the numeric accumulator changes the operation into string concatenation, producing an incorrect total. Formatting should be applied after the numeric sum is calculated.
