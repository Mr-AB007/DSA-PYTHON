# LeetCode 142: Linked List Cycle II
# Problem: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return None.
# Approach: Floyd’s Tortoise and Hare algorithm (two-pointer technique)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Method 1: Early return inside the loop when cycle is found
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # Phase 2: Find entry point of cycle
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow  # Start of cycle

        return None  # No cycle found

    # Method 2: More traditional approach using break + post-check
    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        # Phase 1: Detect cycle with break
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # If no cycle detected (loop didn't break due to meeting point)
        if not fast or not fast.next:
            return None

        # Phase 2: Find entry point of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # Start of cycle
