import functools

@functools.lru_cache()
def countWays(n):
    print('countWays(%s) called.' % (n))
    if n < 0:
        print('countWays(%s) returned 0.' % (n))
        return 0
    elif n == 0:
        print('countWays(0) returned 1.')
        return 1
    else:
        result = countWays(n - 1) + countWays(n - 2) + countWays(n - 3)
        print('countWays(%s) returned %s.' % (n, result))
        return result

print(countWays(20))