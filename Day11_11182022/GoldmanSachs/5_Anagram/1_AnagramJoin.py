
#Functions
def groupAnagram(strs):
    hashMap = {}
    for s in strs:
        temp = "".join(sorted(s))
        if temp in hashMap:
            hashMap[temp].append(s)
        else:
            hashMap[temp] = [s]
    return hashMap.values()
#Drivers Code
strs = ["eat","tea","tan","ate","nat","bat"]
# # strs = ["",""]
# strs = ["compilations","complainants"]
print(groupAnagram(strs))