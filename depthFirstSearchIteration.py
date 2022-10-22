root = {'name': 'Alice', 'children': [{'name': 'Bob', 'children': [{'name': 'Darya', 'children': []}]}, {'name': 'Caroline', 'children': [{'name': 'Eve', 'children': [{'name': 'Gonzalo', 'children': []}, {'name': 'Hadassah', 'children': []}]}, {'name': 'Fred', 'children': []}]}]}

def find8LetterName(root):
    stack = [root]

    while len(stack) != 0:
        node = stack.pop()
        print('Searching node ' + node['name'] + '...')

        if len(node['name']) == 8:
            return node['name']

        for childNode in reversed(node['children']):
            # Preorder depth-first search:
            #stack.append(childNode)

            # Postorder depth-first search:
            stack.insert(0, childNode)

    # Value was not found or there are no children.
    return None  # BASE CASE

print('Found an 8-letter name: ' + str(find8LetterName(root)))
