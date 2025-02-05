
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x%10 == 0):
            return False
        temp = x
        rev = 0
        while temp > 0:
            rev = rev*10 + temp%10
            temp //= 10
        return True if rev == x else False

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [121, -121, 10, 0, 1221, 12321, 1001, 123]

    for num in test_cases:
        result = solution.isPalindrome(num)
        print(f"isPalindrome({num}) -> {result}")