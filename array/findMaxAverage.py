//slinding window pattern
//643. Maximum Average Subarray I

def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        max_sum = sums/k

        for i in range(k,len(nums)):
            sums+= nums[i] - nums[i-k]
            if sums/k > max_sum:
                max_sum = sums/k
        return max_sum
