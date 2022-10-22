root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

def postorderTraverse(node):
    if len(node['children']) > 0:
        # RECURSIVE CASE
        for child in node['children']:
            postorderTraverse(child)  # Traverse child nodes.
    print(node['data'], end=' ')  # Access this node's data.
    # BASE CASE
    return

postorderTraverse(root)
