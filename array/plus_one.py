"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

def plusOne(digits):
    # Iterate from the last digit to the first one (right to left)
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1  # Increase the digit
            return digits  # Return the updated array

        digits[i] = 0  # If the digit is 9, set it to 0 (carry over)

    # If all digits were 9, create a new array with an extra space
    return [1] + digits  # Example: [9,9,9] → [1,0,0,0]


# Example usage:
digits = [9, 9, 9]
print(plusOne(digits))# Output: [1, 0, 0, 0]
print(plusOne([9,9,8,9,9]))
