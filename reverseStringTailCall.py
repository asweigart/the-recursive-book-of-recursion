def rev(theString, accum=''):
    if len(theString) == 0:
        # BASE CASE
        return accum
    else:
        # RECURSIVE CASE
        head = theString[0]
        tail = theString[1:]
        return rev(tail, head + accum)

text = 'abcdef'
print('The reverse of ' + text + ' is ' + rev(text))
text = 'Hello, world!'
print('The reverse of ' + text + ' is ' + rev(text))
text = ''
print('The reverse of ' + text + ' is ' + rev(text))
text = 'X'
print('The reverse of ' + text + ' is ' + rev(text))
