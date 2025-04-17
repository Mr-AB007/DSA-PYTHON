class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

# Example usage:
# nums = [-2, 0, 3, -5, 2, -1]
# obj = NumArray(nums)
# print(obj.sumRange(0, 2))  # Output: 1
# print(obj.sumRange(2, 5))  # Output: -1
# print(obj.sumRange(0, 5))  # Output: -3




class NumArray:
    def __init__(self, nums):
        # Initialize prefix sum array
        self.prefixsum = [0] * len(nums)
        self.prefixsum[0] = nums[0]
        
        # Fill in the prefix array such that prefixsum[i] stores the sum of elements from 0 to i
        for i in range(1, len(nums)):
            self.prefixsum[i] = self.prefixsum[i - 1] + nums[i]

    def sumRange(self, left, right):
        # If the range starts from index 0, return prefixsum[right] directly
        if left == 0:
            return self.prefixsum[right]
        
        # Otherwise, subtract the prefix sum up to left-1 to get the range sum
        return self.prefixsum[right] - self.prefixsum[left - 1]

# Example usage:
# nums = [-2, 0, 3, -5, 2, -1]
# obj = NumArray(nums)
# print(obj.sumRange(0, 2))  # Output: 1
# print(obj.sumRange(2, 5))  # Output: -1
# print(obj.sumRange(0, 5))  # Output: -3
