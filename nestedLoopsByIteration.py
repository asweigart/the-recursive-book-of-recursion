for a in range(1, 5): # The outer loop.
    print('Multiples of ' + str(a))
    for b in range(1, 6): # The inner loop.
        print('%s times %s is %s' % (a, b, a * b))
