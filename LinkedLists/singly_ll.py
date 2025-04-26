class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(12)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentnode = node1
while currentnode:
    print(currentnode.data, end= " --> ")
    currentnode = currentnode.next
print("null")

