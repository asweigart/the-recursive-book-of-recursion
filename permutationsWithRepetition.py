def getPermsWithRep(chars, permLength=None, prefix=''):
    indent = '.' * len(prefix)
    print(indent + 'Start, args=("' + chars + '", ' + str(permLength) + ', "' + prefix + '")')
    if permLength is None:
        permLength = len(chars)

    # BASE CASE
    if (permLength == 0):
        print(indent + 'Base case reached, returning', [prefix])
        return [prefix]

    # RECURSIVE CASE
    # Create a new prefix by adding each character to the current prefix.
    results = []
    print(indent + 'Adding each char to prefix "' + prefix + '".')
    for char in chars:
        newPrefix = prefix + char

        # Decrease permLength by one because we added one character to the prefix.
        results.extend(getPermsWithRep(chars, permLength - 1, newPrefix))
    print(indent + 'Returning', results)
    return results


print('All permutations with repetition of JPB123:')
print(getPermsWithRep('JPB123', 4))
