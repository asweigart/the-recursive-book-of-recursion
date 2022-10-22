import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def quickselect(items, kth, left=None, right=None):
    # By default, `left` and `right` span the entire range of `items`.
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1 # `right` defaults to the last index in items.

    if (len(items) == 0) or (not (0 <= kth < len(items))):
        return None



    if left == right:
        return items[left] # BASE CASE

    logging.debug(f'pivot/leftval={items[left]}, rightval={items[right]} items={items}')

    # Partition step:
    i = left
    for j in range(left + 1, right + 1):
        logging.debug(f'i={i}, j={j}, left={left}, comparing {items[j]} < {items[left]}')
        if items[j] < items[left]:
            i += 1
            items[i], items[j] = items[j], items[i]
            logging.debug(f'i={i}, j={j}, swapped i and j: {items[i]} and {items[j]}, items={items}')

    # Move the pivot to the correct location:
    items[i], items[left] = items[left], items[i]

    # Recursively partition one side only:
    if kth == i: # We've sorted kth items in `items`.
        return items[i] # BASE CASE
    elif i < kth: # TODO We haven't "sorted" enough of `items`, sort items to the right of the pivot.
        return quickselect(items, kth, i + 1, right) # RECURSIVE CASE
    else: # We've "sorted" too many
        return quickselect(items, kth, left, i - 1) # RECURSIVE CASE


#a = [6, 0, 2, 16, 14, 10, 18, 20, 12, 4, 8] # kth == i case
a = [18, 20, 14, 16, 4, 10, 6, 2, 8, 0, 12]
print(a)
logging.debug(f'Searching for kth of 3 in {a}')
print(quickselect(a, 3))
print(a)
