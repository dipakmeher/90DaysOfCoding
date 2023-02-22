# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

# Status: Completed
def groupAnagram(strs):
    # with key as sorted string
    res = {}
    for i in strs:
        srt = "".join(sorted(i))
        if srt in res:
            res[srt].append(i)
        else:
            res[srt] = [i]
    return res.values()

#Drivers Code
#strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["",""]
strs = ["compilations","complainants"]
print(groupAnagram(strs))
