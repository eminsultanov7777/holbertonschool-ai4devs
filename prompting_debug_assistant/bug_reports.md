# Bug Reports

This document summarizes the five defects, their root causes, the applied resolutions, and the lessons learned during AI-assisted debugging.

## Bug Report – bug1.py

- **File Name**: `bug1.py` (corrected version: `bug_fixes/bug1_fixed.py`)
- **Bug Summary**: The average-calculation program could not run because it contained a Python syntax error.
- **Root Cause**: The `if len(numbers) == 0` statement was missing a colon (`:`), which is required before an indented block in Python.
- **Resolution**:
  - **AI-generated suggestion**: Add the missing colon and retain the empty-list check.
  - **Manual edits**: Added assertions for a regular list and an empty list to verify the behavior.
  - **Final behavior**: `[10, 20, 30, 40]` returns `25.0`; an empty list returns `0`.
- **Lessons Learned**: Small syntax mistakes prevent a program from running at all. Run or compile code after editing, and test boundary cases such as empty input.

## Bug Report – bug2.js

- **File Name**: `bug2.js` (corrected version: `bug_fixes/bug2_fixed.js`)
- **Bug Summary**: The registration function incorrectly rejected users who were exactly 18 years old.
- **Root Cause**: The condition `age > 18` excluded the boundary value 18, although the requirement was to allow users aged 18 and older.
- **Resolution**:
  - **AI-generated suggestion**: Change the comparison from `>` to `>=`.
  - **Manual edits**: Added explicit checks for ages 17, 18, and 19.
  - **Final behavior**: Ages 17 are rejected; ages 18 and 19 are accepted.
- **Lessons Learned**: Requirements involving minimum or maximum values need boundary-value tests. A single comparison operator can change the behavior at the boundary.

## Bug Report – bug3.py

- **File Name**: `bug3.py` (corrected version: `bug_fixes/bug3_fixed.py`)
- **Bug Summary**: Looking up a username that did not exist caused the program to terminate with an exception.
- **Root Cause**: Direct dictionary access with `users[username]` raises `KeyError` when the requested key is absent. The sample requested `samir`, which was not present in the dictionary.
- **Resolution**:
  - **AI-generated suggestion**: Use `dict.get()` and handle a missing value before processing the email.
  - **Manual edits**: Added tests for both an existing username (`aylin`) and a missing username (`samir`).
  - **Final behavior**: Existing users receive their lowercase email address; a missing user returns `None` without crashing.
- **Lessons Learned**: External or user-provided lookup values may be missing. Handle absent dictionary keys explicitly instead of assuming every key exists.

## Bug Report – bug4.c

- **File Name**: `bug4.c` (corrected version: `bug_fixes/bug4_fixed.c`)
- **Bug Summary**: The array-printing loop attempted to read one element beyond the end of the array.
- **Root Cause**: The loop used `i <= length`. For an array with `length` elements, valid indexes are `0` through `length - 1`; index `length` is out of bounds and accessing it causes undefined behavior in C.
- **Resolution**:
  - **AI-generated suggestion**: Change the loop condition to `i < length`.
  - **Manual edits**: Compiled the corrected C program and checked that its output contained exactly the five array values.
  - **Final behavior**: The program prints `4`, `8`, `12`, `16`, and `20`, each once.
- **Lessons Learned**: Array bounds must be respected. Prefer loop conditions that stop before the element count, and compile and test C programs after changing index logic.

## Bug Report – bug5.js

- **File Name**: `bug5.js` (corrected version: `bug_fixes/bug5_fixed.js`)
- **Bug Summary**: The shopping-cart total was calculated incorrectly because the accumulator could become a string.
- **Root Cause**: JavaScript's `toFixed(2)` returns a string. Adding that string to the numeric `total` causes string concatenation instead of numeric addition.
- **Resolution**:
  - **AI-generated suggestion**: Add the numeric prices first and call `toFixed(2)` only once after the loop.
  - **Manual edits**: Added checks for the sample cart and an empty cart.
  - **Final behavior**: The sample cart returns `"10.00"` and an empty cart returns `"0.00"`.
- **Lessons Learned**: Be aware of return types from library methods. Keep calculations numeric and format values only when preparing the final output.

## Overall Lessons Learned

- AI can quickly identify common syntax, logic, runtime, boundary, and data-type issues, but suggested fixes still need to be checked against requirements.
- Tests should cover normal inputs, edge cases, and invalid or missing data.
- Distinguish between the AI-proposed correction and manual validation work.
- Record the observed results so that future developers can understand why a change was made.
