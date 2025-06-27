from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    
    def __init__(self, root_val):
        self.root = TreeNode(root_val)
    
    def dfs_preorder(self, node):
        if not node:
            return
        print(node.val, end=' ->')
        self.dfs_preorder(node.left)
        self.dfs_preorder(node.right)
        
    def dfs_inorder(self, node):
        if not node:
            return
        self.dfs_inorder(node.left)
        print(node.val, end=' -> ')
        self.dfs_inorder(node.right)
    
    def dfs_postorder(self, node):
        if not node:
            return
        self.dfs_postorder(node.left)
        self.dfs_postorder(node.right)
        print(node.val, end=' -> ')
        
    def bfs(self, node):
        if not node:
            return
        
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node.val, end=' --> ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        

tree = BinaryTree("A")
tree.root.left = TreeNode("B")
tree.root.right = TreeNode("C")
tree.root.left.left = TreeNode("D")
tree.root.left.right = TreeNode("E")
tree.root.right.right = TreeNode("F")

# Perform DFS Traversals
print("Preorder Traversal:")
tree.dfs_preorder(tree.root)     # Output: A B D E C F

print("\nInorder Traversal:")
tree.dfs_inorder(tree.root)      # Output: D B E A C F

print("\nPostorder Traversal:")
tree.dfs_postorder(tree.root)    # Output: D E B F C A

print("\n BFS")
tree.bfs(tree.root)