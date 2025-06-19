'''
# Creating a Sample Linked List : Practice.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# 2.Create Values/ data for Nodes
node1 = Node(3)
node2 = Node(5)
node3 = Node(12)
node4 = Node(2)

#3. Link the node to next node
node1.next = node2
node2.next = node3
node3.next = node4

#4. Look at Current Node and Print
currentNode = node1
while currentNode:
    print(currentNode.data, end=" --> ")
    currentNode = currentNode.next
print("null")

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after(self, prev_value, data):
        curr = self.head
        while curr and curr.data != prev_value:
            curr = curr.next
        if not curr:
            print(f'Node with{prev_value} not found')
            return
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node
        
    def delete(self, key):
        curr = self.head
        