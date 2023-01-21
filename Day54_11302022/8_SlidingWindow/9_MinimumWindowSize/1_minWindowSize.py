def MinWindowSize(str,substr, n,k):
    hashMap = dict()
    for i in substr:
        if i in hashMap:
            hashMap[i] +=1
        else:
            hashMap[i] = 1
    count = len(hashMap)
    print(hashMap)
    i = 0
    j = 0
    ans = 0
    mn = 100000
    while(j<n):
        #Calculations
        if str[j] in hashMap:
            hashMap[str[j]] -=1
            if(hashMap[str[j]] == 0):
                count-=1 
            print(hashMap)
        if(count>0):
            j+=1
        elif(count==0):
            mn = min(mn,j-i+1)
            print("mn = ", mn)
            while(i<=j):
                if str[i] in hashMap:
                    hashMap[str[i]] +=1
                    if(hashMap[str[i]] >= 1):
                        count+=1 
                i+=1
            # print(hashMap)
            i+=1
            j+=1
    print("Minimum Substring with consisting key is", mn)   
    

#Driver Code
str = "foxyrxyofyzrofor"
key = "for"
n = len(str)
k = len(key)
MinWindowSize(str, key,n,k)