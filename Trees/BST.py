class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)
    
    def Search(self, node, target):
        if node is None:
            return None
        elif node.value == target:
            return node
        elif target < node.value:
            return self.Search(node.left, target)
        else:
            return self.Search(node.right, target)
        
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

result = bst.Search(bst.root, 70)
if result:
    print(f'Found: {result.value}')
else:
    print('not found')

print(result.value)