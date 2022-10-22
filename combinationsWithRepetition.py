def getCombosWithRepetition(chars, k, startFrom=None, prefix=None, results=None):
    if startFrom is None:
        startFrom = chars[0]
    if prefix is None:
        prefix = []
    if results is None:
        results = []

    if len(prefix) == k:
        # BASE CASE
        results.append(''.join(prefix))
        return

    # RECURSIVE CASE
    for char in chars[chars.find(startFrom):]:
        prefix.append(char)
        getCombosWithRepetition(chars, k, char, prefix, results)
        prefix.pop()
    return results

#print(getCombosWithRepetition('ABC', 3))



def getCombosWithRep2(chars, k):
    combos = []
    prefix = [chars[0]] * k

    # Replace top of prefix with the next letter, of if it's the last letter, pop it.
    while True:
        combos.append(''.join(prefix))

        while ''.join(prefix[-1]) == chars[-1]:
            prefix.pop()
            if prefix == []:
                return combos

        nextCharIndex = chars.find(prefix[-1]) + 1
        prefix[-1] = chars[nextCharIndex]

        while len(prefix) < k:
            prefix.append(prefix[-1])


def getPermsWithRep2(chars, k):
    combos = []
    prefix = [chars[0]] * k

    # Replace top of prefix with the next letter, of if it's the last letter, pop it.
    while True:
        combos.append(''.join(prefix))

        while ''.join(prefix[-1]) == chars[-1]:
            prefix.pop()
            if prefix == []:
                return combos

        nextCharIndex = chars.find(prefix[-1]) + 1
        prefix[-1] = chars[nextCharIndex]

        while len(prefix) < k:
            prefix.append(chars[0])

print(getCombosWithRep2('ABC', 1))
print(getCombosWithRep2('ABC', 2))
print(getCombosWithRep2('ABC', 3))
#print(getPermsWithRep2('ABC', 3))