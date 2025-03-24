"""
203. Remove Linked List Elements

Problem Statement:
Given the head of a linked list and an integer `val`, remove all nodes of the linked list that have `Node.val == val`, and return the new head.
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  #Time O(n)
  #Space O(1)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(-1,head)
        temp = node
        while temp.next:
            if temp.next and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return node.next
      
#recursion but it is bad in python means performance
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None;
        head.next = self.removeElements(head.next,val)
        return head.next if head.val == val else head
