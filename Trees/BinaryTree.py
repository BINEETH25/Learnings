'''
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
if __name__ == "__main__":
    tree = BinaryTree()
    
    tree.root = TreeNode(10)
    tree.root.left = TreeNode(5)
    tree.root.right = TreeNode(20)

    tree.root.left.left = TreeNode(3)
    tree.root.left.right = TreeNode(7)

    tree.root.right.left = TreeNode(15)
    tree.root.right.right = TreeNode(25)
    
    print(tree.root)
    
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end = ", ")
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end = ", ")

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
preOrderTraversal(root)
print("\n")
inOrderTraversal(root)
print("\n")
postOrderTraversal(root)
print("\n")

