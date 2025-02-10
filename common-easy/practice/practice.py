str1 = "Hello"
arr = [4, 1, 9, 2]

def find_max(arr:list) -> int :
    arr.sort()
    return arr[-1] #return last element

#Plaindrome check for string
def isPalindrome(s: str) -> bool:  # Fixed the typo in the function name
    return s == s[::-1] 

def main():
    # print(str1[::-1])
    # print(str1[3:1:-1])
    # print(find_max(arr))
    # print(isPalindrome("31221"))
    # s = "abcdef"
    # print(s[1:5])   # bcde
    # print(s[:4])    # abcd
    # print(s[2:])    # cdef
    # print(s[:-1])   # abcde
    # print(s[::-2])  # fdb
    # print("abcdefg"[::-3])  # gdb
    # print("OpenAI"[::-1])   # IAnepO
    # print("SlicingPython"[1::2]) # lcnPto

if __name__ == "__main__":
    main()