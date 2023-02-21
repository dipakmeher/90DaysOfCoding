def checkAnagram(s1,s2):
    if(len(s1) == 0 and len(s2) == 0):
        return True
    for i in s1:
        if(s1.count(i) != s2.count(i)):
            return False
        return set(s1) == set(s2) and len(s1) == len(s2)

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