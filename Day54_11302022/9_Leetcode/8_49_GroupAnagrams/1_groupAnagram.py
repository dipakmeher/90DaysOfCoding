# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Status: Incomplete
#Functions
def checkAnagram(s,t):
    a = {}
    b = {}
    for i in s:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    for i in t:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    if a == b:
        return True
    else:
        return False
    # if(len(s1) == 0 and len(s2) == 0):
    #     return True
    # for i in s1:
    #     if(s1.count(i) != s2.count(i)):
    #         return False
    #     return set(s1) == set(s2) and len(s1) == len(s2)

def groupAnagram(strs):
    n = len(strs)
    res = []
    res.append([strs[0]])
    flag = False
    for i in range(1,n):
        count = 0
        flag = False
        for j in range(len(res)):
            print(strs[i])
            count+=1
            print(count)
            if(checkAnagram(res[j][0],strs[i])):
                res[j].append(strs[i])
                flag = True
                break
        if(flag == False):
            res.append([strs[i]])
        print(res)
    return res
            


#Drivers Code
#strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["",""]
strs = ["compilations","complainants"]
print(groupAnagram(strs))
