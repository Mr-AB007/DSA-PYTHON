# Python implementation with a more optimized approach
def is_valid(s: str) -> bool:
    if len(s) < 2:
        return False

    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []

    for c in s:
        if c in brackets.values():  # Opening bracket
            stack.append(c)
        elif c in brackets:  # Closing bracket(keys)
            if not stack or stack.pop() != brackets[c]:
                return False

    return not stack


# Example Usage
print(is_valid("{[()]}"))  # Output: True
print(is_valid("{[(])}"))  # Output: False
