class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BuildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    mid = inorder.index(root_val)
    
    root.left = BuildTree(preorder[1:mid+1], inorder[:mid])
    root.right = BuildTree(preorder[mid+1:], inorder[mid+1:])
    
    return root

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

tree = BuildTree(preorder, inorder)

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.value, end=", ")
        printInOrder(root.right)

print("Inorder of Constructed Tree:")
printInOrder(tree)
print("\n")