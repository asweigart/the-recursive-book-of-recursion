def gcd(a, b):
    a, b = b % a, a
    if a == 0:
        # BASE CASE
        return b
    else:
        # RECURSIVE CASE
        return gcd(a, b)

print(gcd(42, 28))
print(gcd(28, 42))
print(gcd(345, 766))
