def summation(numbers, i=0, accumulator=0):
    if i == len(numbers):
        # BASE CASE
        return accumulator
    else:
        # RECURSIVE CASE
        return summation(numbers, i + 1, accumulator + numbers[i])

print(summation([1, 2, 3, 4, 5]))
print(summation([5, 2, 4, 8]))
print(summation([1, 10, 100, 1000]))
