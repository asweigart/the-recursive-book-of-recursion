def binarySearch(needle, haystack, left=None, right=None):
    # By default, `left` and `right` are all of `haystack`:
    if left is None:
        left = 0  # `left` defaults to the 0 index.
    if right is None:
        right = len(haystack) - 1  # `right` defaults to the last index.

    print('Searching:', haystack[left:right + 1])

    if left > right:  # BASE CASE
        return None  # The `needle` is not in `haystack`.

    mid = (left + right) // 2
    if needle == haystack[mid]:  # BASE CASE
        return mid  # The `needle` has been found in `haystack`
    elif needle < haystack[mid]:  # RECURSIVE CASE
        return binarySearch(needle, haystack, left, mid - 1)
    elif needle > haystack[mid]:  # RECURSIVE CASE
        return binarySearch(needle, haystack, mid + 1, right)

print(binarySearch(13, [1, 4, 8, 11, 13, 16, 19, 19]))
