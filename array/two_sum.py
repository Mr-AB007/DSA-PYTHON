from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}  # Dictionary to store {number: index}

    for i, n in enumerate(nums):  #enumrate keep i as index and n as value i.e in first iteration value of i = 0 and n = 2
        if (target - n) in nums_map:  # Check if complement exists in dictionary
            return [nums_map.get(target - n), i]  # Return earlier index first
        
        nums_map[n] = i  # Store number with its index

    return []  # Return an empty list if no solution is found

# Correct main block
if __name__ == "__main__":
    nums = [2, 7, 10, 11, 8]
    target = 9
    print(twoSum(nums, target))  # Expected Output: [0, 1]

