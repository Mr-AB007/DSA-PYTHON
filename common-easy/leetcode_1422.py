# LeetCode Problem 1422: Maximum Score After Splitting a String
# Problem Statement:
# Given a binary string s, split it into two non-empty substrings such that the score is 
# the number of 0's in the left substring plus the number of 1's in the right substring.
# Return the maximum score achievable.

class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        max_score = 0
        left_zeros = 0
        right_ones = total_ones

        for i in range(len(s) - 1):  # Ensure both parts are non-empty
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            max_score = max(max_score, left_zeros + right_ones)

        return max_score
