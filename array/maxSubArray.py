//KADANE'S ALGORITHM
//53. Maximum subarrray 

def maxSubArray(self, nums: List[int]) -> int:
        maxsum = sums = nums[0]
        for i in range(1,len(nums)):
            sums += nums[i]
            if sums < nums[i]:
                sums = nums[i]
            if maxsum < sums:
                maxsum = sums
        return maxsum
