class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Edge case: If the input list is empty, return an empty string
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Iterate through the remaining strings in the list
        for i in range(1, len(strs)):
            # Keep reducing the prefix until it matches the start of strs[i]
            while strs[i].find(prefix) != 0:  # If prefix is NOT at the start
                prefix = prefix[:-1]  # Remove the last character from prefix
                
                # If prefix becomes empty, return an empty string
                if not prefix:
                    return ""

        # Return the longest common prefix found
        return prefix
