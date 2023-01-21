#Functions
def longestSubstringKUniqueChar(str,n):
    i = 0
    j = 0
    hashMap = dict()
    mx=0
    while(j<n):
        if(str[j] in hashMap):
            hashMap[str[j]] +=1
        else:
            hashMap[str[j]] = 1

        if(hashMap[str[j]] == 1):
            mx = max(mx,j-i+1)
            j+=1
        elif(hashMap[str[j]] > 1):
            while(hashMap[str[j]] > 1):
                hashMap[str[i]] -= 1
                if(hashMap[str[i]]==0):
                    hashMap.pop(str[i])
                i+=1
            j+=1
    print("The longest substring without repeating character is",mx)

#Driver Code
str = "aababebe"
n = len(str)
#condition is without repeating character
longestSubstringKUniqueChar(str,n)