

class continuous_array:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_fre = {0: -1}
        largest = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += 2 * nums[i] - 1

            if prefix_fre.get(prefix_sum) is not None:
                index = i - prefix_fre[prefix_sum]
                if index > largest:
                    largest = index
            else:
                prefix_fre[prefix_sum] = i

        return largest

