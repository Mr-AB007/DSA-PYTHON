#find index of needle string in haystack

def strStr( haystack: str, needle: str) -> int:
    return haystack.find(needle)
    # for i in range(len(haystack) - len(needle) + 1):
    #     if haystack.startswith(needle, i):
    #         return i
    # return -1

print(strStr("a123fcg","123"))