class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None
        
def BuildTree(postorder, inorder):
    if not postorder or not inorder:
        return None
    
    root_val = postorder[-1]
    root = TreeNode(root_val)
    
    mid = inorder.index(root_val)
    root.right = BuildTree(postorder[mid: -1], inorder[mid+1:])
    root.left = BuildTree(postorder[:mid], inorder[:mid])
    
    return root

postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]

tree = BuildTree(postorder, inorder)

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.value, end = ", ")
        inorderTraversal(root.right)

print("Inorder of Constructed Tree:")
inorderTraversal(tree)
print("\n")