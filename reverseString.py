def rev(theString):
    if len(theString) == 0 or len(theString) == 1:
        # BASE CASE
        return theString
    else:
        # RECURSIVE CASE
        head = theString[0]
        tail = theString[1:]
        return rev(tail) + head

text = 'abcdef'
print('The reverse of ' + text + ' is ' + rev(text))
text = 'Hello, world!'
print('The reverse of ' + text + ' is ' + rev(text))
text = ''
print('The reverse of ' + text + ' is ' + rev(text))
text = 'X'
print('The reverse of ' + text + ' is ' + rev(text))
