class ListNode:
    """ Definition for a singly-linked list node """
    def __init__(self, x):
        self.val = x  # Node value
        self.next = None  # Pointer to the next node

def detectCycle(head: ListNode) -> ListNode:
    """
    Detects the start of the cycle in a linked list.
    If there is a cycle, it returns the node where the cycle begins.
    If there is no cycle, it returns None.

    :param head: The head of the linked list
    :return: The node where the cycle starts, or None if no cycle exists
    """
    slow, fast = head, head  # Initialize slow and fast pointers

    # Step 1: Detect if a cycle exists using Floyd’s Cycle Detection Algorithm
    while fast and fast.next:
        slow = slow.next  # Move slow pointer by 1 step
        fast = fast.next.next  # Move fast pointer by 2 steps

        if slow == fast:  # Cycle detected
            slow = head  # Reset slow pointer to the head

            # Step 2: Find the start of the cycle
            while slow != fast:
                slow = slow.next  # Move both pointers one step at a time
                fast = fast.next

            return slow  # Return the start node of the cycle

    return None  # No cycle detected

# Function to test the cycle detection
def main():
    """ Test the detectCycle function """

    # Creating a linked list: 3 → 2 → 0 → -4 → (cycle back to node 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    # Linking nodes to form a cycle
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle back to node2

    # Detect cycle
    cycle_start = detectCycle(node1)

    # Print the start of the cycle
    if cycle_start:
        print("Cycle starts at node with value:", cycle_start.val)
    else:
        print("No cycle detected.")

# Run the test
if __name__ == "__main__":
    main()
