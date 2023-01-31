#Functions
def longestSubstringKUniqueChar(str,n,k):
    i = 0
    j = 0
    hashMap = dict()
    mx=0
    while(j<n):
        if(str[j] in hashMap):
            hashMap[str[j]] +=1
        else:
            hashMap[str[j]] = 1

        if(len(hashMap) < k):
            j+=1
        elif(len(hashMap) == k):
            mx = max(mx,j-i+1)
            j+=1
        elif(len(hashMap) > k):
            while(len(hashMap) > k):
                hashMap[str[i]] -= 1
                if(hashMap[str[i]]==0):
                    hashMap.pop(str[i])
                i+=1
            j+=1
    print("The longest substring with k unique characters is",mx)

#Driver Code
str = "aabacbebebe"
n = len(str)
uniqueCharacter = 3

longestSubstringKUniqueChar(str,n,uniqueCharacter)