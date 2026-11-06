# Fixed Bug 1: Syntax error
# Calculate the arithmetic average of a list of numbers.

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

assert calculate_average([10, 20, 30, 40]) == 25
assert calculate_average([]) == 0
print("Bug 1 tests passed")
