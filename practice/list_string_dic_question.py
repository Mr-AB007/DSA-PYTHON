#Reverse a string and check is palindrome or not
from typing import Sized


def is_palindrome(stringVal) -> bool:
    return True if stringVal == stringVal[::-1] else False

print(f"Output: 1 ->  {is_palindrome("121")}")

'''
Write a function that takes a list of numbers and returns the sum of all the elements.
Input: [1, 2, 3, 4]  
Output: 10
'''
def list_sum(l: list):
    sum = 0
    for i in l:
        sum += i
    return sum

print(f"Output: 2 ->  list_sum = {list_sum([1, 2, 3, 4] )}")

'''
Count Occurrences of Elements in a List
Input: [1, 2, 2, 3, 3, 3, 4]  
Output: {1: 1, 2: 2, 3: 3, 4: 1}
'''

def count_occur(l: list) -> dict:
    countMap = {}
    for i in l:
        if i in countMap:
            countMap[i] += 1
        else:
            countMap[i] = 1
    return countMap

print(f"Output: 3 ->  count_occur: {count_occur([1, 2, 2, 3, 3, 3, 4])}")

'''
Find Longest Word in a List
Input: ["apple", "banana", "cherry"]  
Output: "banana"
'''

def longest_word(lst: list) -> str:
    long_value = ""
    for i in lst:
        if len(long_value) < len(i):
            long_value = i
    return long_value


def longest_word2(lst: list) -> Sized:
    return max(lst, key=len)


print(f"Output: 4 ->  longest_word: {longest_word2(["apple", "banana", "cherry"])}")

'''
Remove Duplicates from a List
Input: [1, 2, 2, 3, 4, 4, 5]  
Output: [1, 2, 3, 4, 5]
'''

def remove_duplicate(lst: list):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

print(f"Output: 5 ->  remove_duplicate: {remove_duplicate([1, 2, 2, 3, 4, 4, 5])}")
