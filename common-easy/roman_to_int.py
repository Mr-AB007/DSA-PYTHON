def roman_to_int(s: str) -> int:
    roman_map = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50,
        'X': 10, 'V': 5, 'I': 1
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Utility function to test the implementation
def main():
    test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    
    for roman in test_cases:
        result = roman_to_int(roman)
        print(f"Roman: {roman} -> Integer: {result}")

if __name__ == "__main__":
    main()
