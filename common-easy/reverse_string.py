"""
    Problem Statement:
    Given a list of characters, reverse the list in-place.

    Example:
    Input: ['h', 'e', 'l', 'l', 'o']
    Output: ['o', 'l', 'l', 'e', 'h']
    """

def reverse_string(s:list):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] =  s[right] , s[left] #swaping
        left += 1
        right -= 1

# Utility Main
if __name__ == "__main__":
    s = ['h', 'e', 'l', 'l', 'o']
    print("Original:", s)
    reverse_string(s)
    print("Reversed:", s)

    #one line answer
    print("Again Reversed:",s[::-1])