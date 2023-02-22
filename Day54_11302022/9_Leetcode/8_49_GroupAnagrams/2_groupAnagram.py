# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

# Status: Completed
def groupAnagram(strs):
    res = defaultdict(list)
    for i in strs:
        ct = [0] * 26
        for char in i:
            ct[ord(char) - ord("a")]+=1
        res[tuple(ct)].append(i)
    return res.values()

#Drivers Code
#strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["",""]
strs = ["compilations","complainants"]
print(groupAnagram(strs))
