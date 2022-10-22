def getPowerSet(chars, indent=0):
    debugMsg = '.' * indent + 'In getPowerSet("' + chars + '")'
    print(debugMsg + ', start.')

    if chars == '':
        # BASE CASE
        print(debugMsg + " base case returns ['']")
        return ['']

    # RECURSIVE CASE
    powerSet = []
    head = chars[0]
    tail = chars[1:]

    # First part, get the sets that don't include the head:
    print(debugMsg, "part 1, get sets without head '" + head + "'")
    tailPowerSet = getPowerSet(tail, indent + 1)

    # Second part, get the sets that include the head:
    print(debugMsg, "part 2, get sets with head '" + head + "'")
    for tailSet in tailPowerSet:
        print(debugMsg, 'New set', head + tailSet)
        powerSet.append(head + tailSet)

    powerSet = powerSet + tailPowerSet
    print(debugMsg, 'returning', powerSet)
    return powerSet

print('The power set of ABC:')
print(getPowerSet('ABC'))
