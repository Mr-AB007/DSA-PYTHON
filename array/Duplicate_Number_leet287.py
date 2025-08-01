# LeetCode #287 - Find the Duplicate Number
# Intuition:
# Use Floyd's Tortoise and Hare (Cycle Detection) algorithm. ###
# The array values can be seen as pointers creating a linked list with a cycle,
# where the duplicate number is the entry point of the cycle.
# The first phase finds an intersection point in the cycle.
# The second phase finds the entrance to the cycle, which is the duplicate.

from typing import List

def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Find the intersection point in the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle (duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
