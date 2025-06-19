class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree():
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
    
    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.value, end=", ")
            self.inOrder(node.right)
    
    def preOrder(self, node):
        if node:
            print(node.value, end=", ")
            self.inOrder(node.left)
            self.inOrder(node.right)
    
    def postOrder(self, node):
        if node:
            self.inOrder(node.left)
            self.inOrder(node.right)
            print(node.value, end=", ")
    
    def Search(self, node, target):
        if node is None:
            return None
        elif node.value == target:
            return node
        elif target < node.value:
            return self.Search(node.left, target)
        else:
            return self.Search(node.right, target)
        

bst = BinarySearchTree()

values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

print("Inorder Traversal (Sorted):")
bst.inOrder(bst.root)

print("\nPreorder Traversal:")
bst.preOrder(bst.root)

print("\nPostorder Traversal:")
bst.postOrder(bst.root)
print("\n")

result = bst.Search(bst.root, 70)
if result:
    print(f"Found the node with value: {result.value}")
else:
    print("Value not found in the BST.")