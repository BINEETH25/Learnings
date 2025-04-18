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