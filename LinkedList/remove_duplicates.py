from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        while current and current.next:

            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def print_list(self,head):
        current = head
        while current:
            print(f"{current.val} -> ",end="")
            current = current.next
        print("null")
def main():
    linked_list = ListNode(1,ListNode(1,ListNode(2,ListNode(2))))
    solution = Solution()
    print(f"Original List: ",end="")
    solution.print_list(linked_list)

    solution.deleteDuplicates(linked_list)

    print(f"Final List: ", end="")
    solution.print_list(linked_list)


if __name__ == "__main__":
    main()
