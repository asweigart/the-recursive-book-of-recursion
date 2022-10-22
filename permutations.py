def getPerms(chars, indent=0):
    print('.' * indent + 'Start of getPerms("' + chars + '")')
    if len(chars) == 1:
        # BASE CASE
        print('.' * indent + 'When chars = "' + chars + '" base case returns', chars)
        return [chars]

    # RECURSIVE CASE
    permutations = []
    head = chars[0]
    tail = chars[1:]
    tailPermutations = getPerms(tail, indent + 1)
    for tailPerm in tailPermutations:
        print('.' * indent + 'When chars =', chars, 'putting head', head, 'in all places in', tailPerm)
        for i in range(len(tailPerm) + 1):
            newPerm = tailPerm[0:i] + head + tailPerm[i:]
            print('.' * indent + 'New permutation:', newPerm)
            permutations.append(newPerm)
    print('.' * indent + 'When chars =', chars, 'results are', permutations)
    return permutations

print('Permutations of "ABCD":')
print('Results:', ','.join(getPerms('ABCD')))
