# LeetCode 238: Product of Array Except Self
# Given an integer array nums, return an array answer such that
# answer[i] is the product of all the elements of nums except nums[i]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize prefix and suffix product arrays
        prefix = [1] * n  # prefix[i] will hold product of all elements before i
        suffix = [1] * n  # suffix[i] will hold product of all elements after i
        final = [1] * n   # final result array

        # Build prefix product array
        # prefix[i] = nums[0] * nums[1] * ... * nums[i-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix product array (from right to left)
        # suffix[i] = nums[i+1] * nums[i+2] * ... * nums[n-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Multiply prefix and suffix to get the final result
        for i in range(n):
            final[i] = prefix[i] * suffix[i]

        return final
