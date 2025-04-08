# Definition for singly-linked list.
from typing import Optional


class ListNode:
    """Definition for a singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val  # Node value
        self.next = next  # Pointer to the next node

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

    res = ListNode(0,head)

    fast = res
    slow = res

    # for i in range(0,n+1):
    #     fast = fast.next

    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return res.next

