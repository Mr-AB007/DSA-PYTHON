#Find length of last word
#Given a string s consisting of words and spaces, return the length of the last word in the string.
def findlen(s:str)->int:
    s = s.rstrip()  # Remove trailing spaces
    length = 0

    # Traverse from the end until a space is encountered
    i = len(s) - 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length
    #return len(s.rstrip().split()[-1]    #one line answer  ( .split() → Splits the string into a list of words.)

s = "Hello World  "  # Example string with trailing spaces
print(findlen(s))  # Output: 5
print(len(s.strip().split()[-1]))
