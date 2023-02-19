#Scrambled String
#Status: Incomplete: Not running as per expectations
# import sys
# sys.setrecursionlimit(10000)
#function
def isScrambled(s1,s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if len(s1) <= 1: # = to handle the case a = b
        return False

    for k in range(1,n): 
        #for swapped
        if(isScrambled(s1[:k], s2[n-k:]) and isScrambled(s1[k:],s2[:n-k])): # we dont have to equate but have to paas the two parameter into isScrambled function
            return True
        # for not swapped
        if(isScrambled(s1[:k],s2[:k]) and isScrambled(s1[k:],s2[k:])):
            return True 
    return False

#Driver code
# s1 = "great"
# s2 = "etagr"
s1 = "anagram"
s2 = "nagaram"
n = len(s1)
print("Are s1 and s2 scrambled strings?,", isScrambled(s1,s2))
