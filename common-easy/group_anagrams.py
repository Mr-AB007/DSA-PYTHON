from collections import defaultdict
from typing import List


def group_anagrams(srlist : list)-> list:
    map = {}
    for s1 in srlist:
        s = "".join(sorted(s1))
        if not map.get(s):
            map[s] = []
        map[s].append(s1)
    return list(map.values())

def group_anagrams2( strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)

    for s in strs:
        sorted_key = "".join(sorted(s))  # Sort and use as key
        anagram_map[sorted_key].append(s)

    return list(anagram_map.values())  # Return grouped anagrams

print(group_anagrams2(["ate","tea","bat","tab"]))