def isOdd(number):
    if number == 0:
        # BASE CASE
        return False
    else:
        # RECURSIVE CASE
        return not isOdd(number - 1)

print(isOdd(42))
print(isOdd(99))

def isOddTailCall(number, inversionAccum=False):
    if number == 0:
        # BASE CASE
        return inversionAccum
    else:
        # RECURSIVE CASE
        return isOddTailCall(number - 1, not inversionAccum)

print(isOddTailCall(42))
print(isOddTailCall(99))
