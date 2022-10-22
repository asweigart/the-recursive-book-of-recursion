import sys
sys.setrecursionlimit(2000) # You really can't set it much higher than this without crashing, but even this isn't good enough for (4, 3)

ACKERMANN_CACHE = {}

def ackermannWithCache(m, n, indentation=None):
    if (m, n) in ACKERMANN_CACHE:
        return ACKERMANN_CACHE[(m ,n)]

    if indentation is None:
        indentation = 0
    print('%sackermannWithCache(%s, %s)' % (' ' * indentation, m, n))

    if m == 0:
        # BASE CASE
        result = n + 1
        ACKERMANN_CACHE[(m, n)] = result
        return result
    elif m > 0 and n == 0:
        # RECURSIVE CASE
        result = ackermannWithCache(m - 1, 1, indentation + 1)
        ACKERMANN_CACHE[(m, n)] = result
        return result
    elif m > 0 and n > 0:
        # RECURSIVE CASE
        result = ackermannWithCache(m - 1, ackermannWithCache(m, n - 1, indentation + 1), indentation + 1)
        ACKERMANN_CACHE[(m, n)] = result
        return result

"""
print('Starting with m = 1, n = 1:')
ackermannWithCache(1, 1)
print('Starting with m = 2, n = 3:')
ackermannWithCache(2, 3)
print('Starting with m = 3, n = 3:')
ackermannWithCache(3, 3)
"""
print('Starting with m = 4, n = 3:')
ackermannWithCache(4, 3)