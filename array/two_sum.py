def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            if (target - n) in nums_map:
                return [i,nums_map.get(target - n)]
            nums_map[n] = i;
        return []  
if _
