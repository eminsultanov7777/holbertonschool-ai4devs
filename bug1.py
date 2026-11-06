# Bug 1: Syntax error
# Intended behavior: Calculate the average of a list of numbers.

def calculate_average(numbers):
    if len(numbers) == 0
        return 0
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

values = [10, 20, 30, 40]
result = calculate_average(values)
print("Average:", result)
