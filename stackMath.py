def isOperator(text):
    if text == '+' or text == '-' or text == '*' or text == '/':
        return True
    else:
        return False

def createOperatorNode(text, i=0):
    """Returns (node, pointer to remainingTextAfterThisTree)"""
    #breakpoint()
    node = {}

    if not isOperator(text[i]):
        raise Exception('Expected operator, not ' + text.split()[i])
    else:
        node['operator'] = text[i]

    i += 1  # Move the text index past the operator.
    while text[i] == ' ':
        i += 1  # Keep moving the text index until it points to a non-space character (either an operator or number).

    if isOperator(text[i]):
        # RECURSIVE CASE
        node['left'], i = createOperatorNode(text, i) # left child is an operator node
    else:
        node['left'] = int(text[i:].split()[0]) # left child is a number
        i += len(str(node['left']))  # Move the text index past the number.
        while text[i] == ' ':
            i += 1  # Keep moving the text index until it points to a non-space character (either an operator or number).

    if isOperator(text[i]):
        # RECURSIVE CASE
        node['right'], i = createOperatorNode(text, i) # right child is an operator node
    else:
        node['right'] = int(text[i:].split()[0]) # right child is a number
        i += len(str(node['right']))  # Move the text index past the number.
        while i < len(text) and text[i] == ' ':
            i += 1  # Keep moving the text index until it points to a non-space character (either an operator or number).

    # BASE CASE
    return node, i


def solveMathTree(node):
    if type(node['left']) == dict:
        # RECURSIVE CASE
        # Replace the node with the number it solves to.
        node['left'] = solveMathTree(node['left'])
    if type(node['right']) == dict:
        # RECURSIVE CASE
        # Replace the node with the number it solves to.
        node['right'] = solveMathTree(node['right'])

    # BASE CASE
    if node['operator'] == '+':
        return node['left'] + node['right']
    elif node['operator'] == '-':
        return node['left'] - node['right']
    elif node['operator'] == '*':
        return node['left'] * node['right']
    elif node['operator'] == '/':
        return node['left'] / node['right']




root = createOperatorNode('+ 2 * 3 4')[0]
root = createOperatorNode('* + 2 3 4')[0]
print(solveMathTree(root))
