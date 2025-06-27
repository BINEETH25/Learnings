class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    curr = head
    result = []
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(result))

# 🧪 Example Usage
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    head = build_linked_list(input_list)
    print("Original List:")
    print_linked_list(head)

    sol = Solution()
    reversed_head = sol.reverseList(head)

    print("Reversed List:")
    print_linked_list(reversed_head)
