def countOccurencesOfAnagram(str,anagram, n,k):
    hashMap = dict()
    for i in anagram:
        if i in hashMap:
            hashMap[i] +=1
        else:
            hashMap[i] = 1
    count = len(hashMap)
    print(hashMap)
    i = 0
    j = 0
    ans = 0
    while(j<n):
        #Calculations
        if str[j] in hashMap:
            hashMap[str[j]] -=1
            if(hashMap[str[j]] == 0):
                count-=1 
            print(hashMap)
        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            if(count == 0):
                ans+=1
            if str[i] in hashMap:
                hashMap[str[i]] +=1
                if(hashMap[str[i]] >= 1):
                    count+=1 
                print(hashMap)
            i+=1
            j+=1
    print("Total Count of Occurences to Anagram is",ans)   
    

#Driver Code
str = "forxyofyzrof"
anagram = "for"
n = len(str)
k = len(anagram)
countOccurencesOfAnagram(str, anagram,n,k)