class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None  # No extra argument


def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while True:
        # Fix the if condition
        if not fast or not fast.next:
            return False  # No cycle

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  # Cycle detected


# Create a linked list without a cycle
node1 = ListNode(2)
node2 = ListNode(3)
node1.next = node2  # 2 → 3 → None

print(hasCycle(node1))  # Output: False
