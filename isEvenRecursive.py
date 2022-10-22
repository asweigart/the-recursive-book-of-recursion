def isEvenRecursive(num):
    if num == 0:  # BASE CASE
        return True
    elif num == 1 or num == -1:  # BASE CASE
        return False

    if num > 0:  # RECURSIVE CASE
        return not isEvenRecursive(num - 1)
    elif num < 0:  # RECURSIVE CASE
        return not isEvenRecursive(num + 1)

print(isEvenRecursive(42))
print(isEvenRecursive(99))
print(isEvenRecursive(0))
print(isEvenRecursive(-4))
