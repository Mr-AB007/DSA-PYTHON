class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum1 = 0
        minSum = 0

        for n in nums:
            sum1 += n
            minSum = min(sum1 , minSum)
        return 1 - (minSum)
        
