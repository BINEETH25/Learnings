class arrayBinaryTree():
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size
    
    def set_root(self, key):
        self.tree[0] = key
    
    def set_left(self, parent_index, key):
        child_index = 2 * parent_index + 1
        if child_index < self.size:
            self.tree[child_index] = key
        else:
            print('Out of Bounds')
    
    def set_right(self, parent_index, key):
        child_index = 2 * parent_index + 2
        if child_index < self.size:
            self.tree[child_index] = key
        else:
            print('Out of Bounds')
    
    def print_tree(self):
        for i, val in enumerate(self.tree):
            if val is not None:
                print(f'Index {i} : {val}')
                
    def preorder(self, index):
        if index >= self.size or self.tree[index] is None:
            return
        print(self.tree[index], end=" ")
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)
    
    def inorder(self, index):
        if index >= self.size or self.tree[index] is None:
            return
        self.inorder(2 * index + 1)
        print(self.tree[index], end=" ")
        self.inorder(2 * index + 2)
    
    def postorder(self, index):
        if index >= self.size or self.tree[index] is None:
            return
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=" ")



bt = arrayBinaryTree(10)
bt.set_root('A')
bt.set_left(0, 'B')
bt.set_right(0, 'C')
bt.set_left(1, 'D')
bt.set_right(1, 'E')
bt.set_left(2, 'F')
bt.set_right(2, 'G')

bt.print_tree()

print("\nPreorder:")
bt.preorder(0)

print("\nInorder:")
bt.inorder(0)

print("\nPostorder:")
bt.inorder(0)

print("\n")