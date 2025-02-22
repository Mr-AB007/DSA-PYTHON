
def addBinaryBitwaise(a: str, b:str) -> str:
    x, y = int(a, 2), int(b, 2)     #int(a,2) covert this string to binary number
    while y:
        x,y = x^y , ( x & y ) << 1
    return bin(x)[2:]      #bin(8) coverts to "0b1000" that's why bin(x)[2:]

def addBinary(a: str, b: str) -> str:
    result = []
    i, j = len(a) - 1, len(b) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry:
        sum_ = carry
        if i >= 0:
            sum_ += int(a[i])
            i -= 1
        if j >= 0:
            sum_ += int(b[j])
            j -= 1

        result.append(str(sum_ % 2))  # Append the binary digit
        carry = sum_ // 2  # Compute the new carry

    return ''.join(result[::-1])  # Reverse the result to get the final sum


# Example Usage:
a = "101"
b = "11"
print(addBinaryBitwaise(a, b))  # Output: "1000"
