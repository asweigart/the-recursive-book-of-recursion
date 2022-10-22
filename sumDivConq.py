def sumDivConq(numbers):
    if len(numbers) == 0:  # BASE CASE
        return 0
    elif len(numbers) == 1:  # BASE CASE
        return numbers[0]
    else:  # RECURSIVE CASE
        mid = len(numbers) // 2
        leftHalfSum = sumDivConq(numbers[0:mid])
        rightHalfSum = sumDivConq(numbers[mid:len(numbers) + 1])
        return leftHalfSum + rightHalfSum

nums = [1, 2, 3, 4, 5]
print('The sum of', nums, 'is', sumDivConq(nums))
nums = [5, 2, 4, 8]
print('The sum of', nums, 'is', sumDivConq(nums))
nums = [1, 10, 100, 1000]
print('The sum of', nums, 'is', sumDivConq(nums))