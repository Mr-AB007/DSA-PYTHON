class Solution:
    # ✅ Method 1: Sliding window using "if i >= k - 1" pattern
    def findMaxAverage1(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]  # Edge case: only one number in the array

        window_sum = 0.0
        max_avg = float('-inf')  # Start with the smallest possible number

        # Iterate through the entire list
        for i in range(n):
            window_sum += nums[i]  # Add current element to the window sum

            # Once we have at least 'k' elements, start calculating averages
            if i >= k - 1:
                # Update max average if this window's average is greater
                max_avg = max(max_avg, window_sum / k)
                # Slide the window: remove the leftmost (oldest) element
                window_sum -= nums[i - k + 1]

        return max_avg


    # ✅ Method 2: Sliding window with pre-computed initial window
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]  # Edge case: only one number

        window_sum = 0.0

        # Step 1: Calculate the sum of the first window of size k
        for i in range(k):
            window_sum += nums[i]

        # Step 2: Initialize max average with the first window's average
        max_avg = window_sum / k

        # Step 3: Slide the window through the rest of the array
        for i in range(k, n):
            # Add new element and remove the element going out of window
            window_sum += nums[i] - nums[i - k]
            # Update max average if current average is greater
            max_avg = max(max_avg, window_sum / k)

        return max_avg
