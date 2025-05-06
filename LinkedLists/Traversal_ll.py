# Forward Traversal of a Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def TraverseandPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end= ' -> ')
        currentNode = currentNode.next
    print('null')

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

TraverseandPrint(node1)

# 1.Finding the Lowest Value in Linkedlist by Traversing forward
def lowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

print("Lowest Value: ", lowestValue(node1))

# 2.Deleting a node in linkedlist
def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next
    curNode = head
    while curNode.next and curNode.next != nodeToDelete:
        curNode = curNode.next
    if curNode.next is None:
        return head
    curNode.next = curNode.next.next
    return head


TraverseandPrint(node1)
node1 = deleteSpecificNode(node1, node3)
print("After Deleting: ")
TraverseandPrint(node1)

# 3.Inserting a Node in Linked list
