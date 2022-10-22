root = {'name': 'Alice', 'children': [{'name': 'Bob', 'children':
[{'name': 'Darya', 'children': []}]}, {'name': 'Caroline',
'children': [{'name': 'Eve', 'children': [{'name': 'Gonzalo',
'children': []}, {'name': 'Hadassah', 'children': []}]}, {'name':
'Fred', 'children': []}]}]}

def find8LetterName(node):
    print('Visiting node ' + node['name'] + '...')

    # Preorder depth-first search:
    #print('Checking if ' + node['name'] + ' is 8 letters...')
    #if len(node['name']) == 8: return node['name']  # BASE CASE

    if len(node['children']) > 0:
        # RECURSIVE CASE
        for child in node['children']:
            returnValue = find8LetterName(child)
            if returnValue != None:
                return returnValue

    # Postorder depth-first search:
    print('Checking if ' + node['name'] + ' is 8 letters...')
    if len(node['name']) == 8: return node['name']  # BASE CASE

    # Value was not found or there are no children.
    return None  # BASE CASE

print('Found an 8-letter name: ' + str(find8LetterName(root)))
