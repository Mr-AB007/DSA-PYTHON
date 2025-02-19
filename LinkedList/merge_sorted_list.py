class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    """ Merge two sorted linked lists into one sorted list by splicing nodes together. """
    if not l1 or not l2:  # If one list is empty, return the other list
        return l1 if l1 else l2

    # Use a dummy node to simplify list merging
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next  # Assign and move l1 forward
        else:
            tail.next, l2 = l2, l2.next  # Assign and move l2 forward
        tail = tail.next  # Move tail forward

    # Attach the remaining part of the non-empty list
    tail.next = l1 if l1 else l2

    return dummy.next  # Return merged list, skipping dummy node

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")

# Example Usage:
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10)))))

merged_head = mergeTwoLists(l1, l2)
printList(merged_head)
