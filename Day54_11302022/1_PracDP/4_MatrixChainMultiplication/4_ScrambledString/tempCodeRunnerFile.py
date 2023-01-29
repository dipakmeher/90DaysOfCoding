  if(isScrambled(s1[:k], s2[n-k:]) and isScrambled(s1[k:],s2[:n-k])): # we dont have to equate but have to paas the two parameter into isScrambled function
            dpDict[temp] = True
            return dpDict[temp]
        # for not swapped
        if(isScrambled(s1[:k],s2[:k]) and isScrambled(s1[k:],s2[k:])):
            dpDict[temp] = True
            return dpDict[temp]
