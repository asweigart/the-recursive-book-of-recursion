def binarySearchIterative(needle, haystack, left=None, right=None):
    # By default, `left` and `right` span the entire range of `haystack`:
    if left is None:
        left = 0  # `left` defaults to the 0 index.
    if right is None:
        right = len(haystack) - 1  # `right` defaults to the last index.

    while True:
        print('Searching:', haystack[left:right + 1])

        if left > right:
            return None  # The `needle` is not in `haystack`.

        mid = (left + right) // 2
        if needle == haystack[mid]:
            return mid  # The `needle` has been found in `haystack`
        elif needle < haystack[mid]:
            right = mid - 1
        elif needle > haystack[mid]:
            left = mid + 1

print(binarySearchIterative(13, [1, 4, 8, 11, 13, 16, 19, 19]))
