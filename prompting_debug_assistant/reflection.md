# Reflection on AI-Assisted Debugging

## Introduction

In this project, I used an AI assistant to investigate five deliberately flawed code snippets written in Python, JavaScript, and C. The examples covered a syntax error, a logic error, a runtime exception, an array-boundary error, and incorrect data-type handling. The goal was to understand each cause, review the suggested correction, and validate the result. This process demonstrated both the practical value of AI and the importance of checking its work.

## AI Strengths

The most direct problems were easiest for the AI to solve. The missing colon in the Python `if` statement had a clear cause and a straightforward correction. The JavaScript age-checking function was similarly simple: changing `age > 18` to `age >= 18` matched the requirement that users aged 18 or older should be allowed. Both explanations were concise and easy to verify with small tests.

The AI was also helpful with language-specific behavior. It explained that accessing a missing Python dictionary key can raise a `KeyError`, and that JavaScript's `toFixed()` method returns a string rather than a number. These explanations connected the symptoms to their underlying causes and provided useful starting points for debugging.

## AI Weaknesses and Trust

The more challenging cases required careful validation. The C array example used `i <= length`, which could access an element beyond the array. Changing the condition to `i < length` was correct, but an out-of-bounds read in C causes undefined behavior, so the original program's output cannot be relied upon. The JavaScript cart example also required understanding how string concatenation differs from numeric addition.

My trust in AI suggestions is conditional, not absolute. AI can identify likely causes quickly, but a plausible explanation may overlook requirements, edge cases, or environment-specific details. In this project, the corrected Python and JavaScript tests passed, and the C program compiled and printed the expected values. These checks were useful, although they covered representative cases rather than every possible input.

## Human Role

Human judgment was necessary to define what “correct” meant. The intended behavior documented for each snippet provided criteria for evaluating the AI's suggestions. I also selected test cases for normal inputs, empty input, missing users, and boundary ages. This was important because code can run without meeting its requirements. I reviewed the proposed changes, compared actual and expected results, and distinguished the AI's suggestions from the validation work.

## Conclusion

AI made the debugging process faster by identifying likely causes, explaining programming-language behavior, and proposing focused fixes. However, it did not replace programming knowledge or testing. The most reliable workflow was to describe the expected behavior, ask AI for an explanation, inspect the proposed change, and run tests to confirm it. In real-world development, AI is a useful assistant for investigation and learning, but developers remain responsible for correctness, security, and maintainability.
