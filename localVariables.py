def a():
    spam = 'Aardvark'
    print('spam is ' + spam)
    b()

def b():
    spam = 'Bobcat'
    print('spam is ' + spam)
    c()

def c():
    spam = 'Coyote'
    print('spam is ' + spam)

a()
