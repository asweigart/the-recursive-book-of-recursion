def findMinValue(numbers):
    if len(numbers) == 0:
        raise Exception('must pass list with at least one number')

    head = numbers[0]
    tail = numbers[1:]

    if len(numbers) == 1:
        # BASE CASE
        return head
    else:
        # RECURSIVE CASE
        minOfTail = findMinValue(tail)
        if head < minOfTail:
            return head
        else:
            return minOfTail

print(findMinValue([0, 1, 2, 3, 4]))
print(findMinValue([1, 2, 3, 4, 0]))
print(findMinValue([1, 2, 0, 3, 4]))
print(findMinValue([42]))
