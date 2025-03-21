def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxVal = 0
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            maxVal = max(maxVal, right - left + 1)
        return maxVal
        
