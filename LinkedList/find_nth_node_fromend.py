class ListNode:
    """Definition for a singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val  # Node value
        self.next = next  # Pointer to the next node


def find_nth_node(head:ListNode, n:int)-> int:
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next

    return slow.val;

if __name__ == "__main__":
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
    #  1 -> 2 -> 3 -> 4 -> 5

    print(find_nth_node(head,4))
