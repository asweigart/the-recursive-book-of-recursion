def quicksort(items, left=None, right=None):
    # By default, `left` and `right` span the entire range of `items`:
    if left is None:
        left = 0  # `left` defaults to the 0 index.
    if right is None:
        right = len(items) - 1  # `right` defaults to the last index.

    print('\nquicksort() called on this range:', items[left:right + 1])
    print('................The full list is:', items)

    if right <= left:
        # With only zero or one items, `items` is already sorted.
        return  # BASE CASE

    # START OF THE PARTITIONING
    i = left  # i starts at the left end of the range.
    pivotValue = items[right]  # Select the last value for the pivot.

    print('....................The pivot is:', pivotValue)

    # Iterate up to, but not including, the pivot:
    for j in range(left, right):
        # If a value is less than the pivot, swap it so that it's on the
        # left side of `items`:
        if items[j] <= pivotValue:
            # Swap these two values:
            items[i], items[j] = items[j], items[i]
            i += 1

    # Put the pivot on the left side of `items`:
    items[i], items[right] = items[right], items[i]
    # END OF THE PARTITIONING

    print('....After swapping, the range is:', items[left:right + 1])
    print('Recursively calling quicksort on:', items[left:i], 'and', items[i + 1:right + 1])

    # Call quicksort() on the two partitions:
    quicksort(items, left, i - 1)   # RECURSIVE CASE
    quicksort(items, i + 1, right)  # RECURSIVE CASE

myList = [0, 7, 6, 3, 1, 2, 5, 4]
quicksort(myList)
print('Sorted:', myList)
