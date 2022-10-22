def sum(numbers):
    if len(numbers) == 0: # BASE CASE
        return 0
    else: # RECURSIVE CASE
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)

nums = [1, 2, 3, 4, 5]
print('The sum of', nums, 'is', sum(nums))
nums = [5, 2, 4, 8]
print('The sum of', nums, 'is', sum(nums))
nums = [1, 10, 100, 1000]
print('The sum of', nums, 'is', sum(nums))