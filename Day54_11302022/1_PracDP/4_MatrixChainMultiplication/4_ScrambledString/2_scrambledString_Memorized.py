#Scrambled String: Memorized
#function
def isScrambled(s1,s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if len(s1) <= 1: # = to handle the case a = b
        return False

    temp = s1+" "+s2
    if(dpDict.keys == temp):
        return dpDict.get(temp)

    for k in range(1,n): 
        #for swapped
        if(isScrambled(s1[:k], s2[n-k:]) and isScrambled(s1[k:],s2[:n-k])):
            # we dont have to equate but have to paas the two parameter into isScrambled function
            dpDict[temp] = True
            return dpDict[temp]
        # for not swapped
        if(isScrambled(s1[:k],s2[:k]) and isScrambled(s1[k:],s2[k:])):
            dpDict[temp] = True
            return dpDict[temp]

    dpDict[temp] = False
    return dpDict[temp]

#Driver code
s1 = "great"
s2 = "etagr"
n = len(s1)

dpDict = {}
print("Are s1 and s2 scrambled strings?,", isScrambled(s1,s2))
