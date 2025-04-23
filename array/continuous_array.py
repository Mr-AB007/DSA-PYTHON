class continuous_array:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_fre = {}
        largest = 1
        prefix_sum = 0

        for i in range(0, len(nums)):
            prefix_sum += 2*nums[i] - 1

            if prefix_fre.get(prefix_sum):
                index = i - prefix_fre[prefix_sum]
                if index > largest:
                    largest = index
            else:
                prefix_fre[prefix_sum] = i
        return largest
