"""You are given two non-empty linked lists representing two non-negative integers. 
 * The digits are stored in reverse order, and each of their nodes contains a single digit. 
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself."""
class ListNode:
    """Definition for a singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val  # Node value
        self.next = next  # Pointer to the next node

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Adds two numbers represented as reversed linked lists and returns the sum as a linked list.
        """
        dummy = ListNode(0)  # Dummy node to simplify result list creation
        current = dummy  # Pointer to build the result linked list
        carry = 0  # Stores carry from previous sum

        # Process both linked lists until both are fully traversed
        while l1 or l2 or carry:
            sum_val = carry  # Start with carry from the previous operation
            
            if l1:
                sum_val += l1.val  # Add digit from first list
                l1 = l1.next  # Move to the next node
            
            if l2:
                sum_val += l2.val  # Add digit from second list
                l2 = l2.next  # Move to the next node

            carry = sum_val // 10  # Compute new carry
            current.next = ListNode(sum_val % 10)  # Create new node with the sum digit
            current = current.next  # Move pointer forward

        return dummy.next  # Return the resulting linked list (excluding the dummy node)

# Helper function to create a linked list from a list of numbers
def create_linked_list(lst):
    """
    Converts a list of numbers into a linked list.
    Example: [2, 4, 3] → 2 -> 4 -> 3
    """
    dummy = ListNode()  # Dummy node to simplify list creation
    current = dummy  # Pointer to build the list
    
    for val in lst:
        current.next = ListNode(val)  # Create new node with current value
        current = current.next  # Move pointer to the new node
    
    return dummy.next  # Return the head of the linked list

# Helper function to print a linked list in a readable format
def print_linked_list(node):
    """
    Prints the linked list in a readable format.
    Example: 2 -> 4 -> 3
    """
    values = []
    while node:
        values.append(str(node.val))  # Store node values in a list
        node = node.next  # Move to the next node
    print(" -> ".join(values))  # Print formatted output

# Function to take user input and create a linked list
def input_linked_list():
    """
    Takes user input as space-separated numbers and converts it into a linked list.
    Example input: 2 4 3 (which represents the number 342 in reverse order)
    """
    lst = list(map(int, input("Enter space-separated digits (in reverse order): ").split()))
    return create_linked_list(lst)  # Convert input into linked list

# Main execution block
if __name__ == "__main__":
    print("Enter first number as a linked list:")
    l1 = input_linked_list()  # Input for first number
    
    print("Enter second number as a linked list:")
    l2 = input_linked_list()  # Input for second number

    solution = Solution()  # Create an instance of the solution class
    result = solution.addTwoNumbers(l1, l2)  # Compute the sum as a linked list

    print("Resultant sum as a linked list:")
    print_linked_list(result)  # Print the final result
