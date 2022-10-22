def outerLoop(a):
    if a < 5:
        # RECURSIVE CASE
        print('Multiples of ' + str(a))
        innerLoop(a, 1)
        outerLoop(a + 1)
        return
    else:
        # BASE CASE
        return

def innerLoop(a, b):
    if b < 6:
        # RECURSIVE CASE
        print('%s times %s is %s' % (a, b, a * b))
        innerLoop(a, b + 1)
        return
    else:
        # BASE CASE
        return

outerLoop(1)