#Functions
#Rev
def firstNegInWindowSizeK(arr, n , k):
    i = 0
    j = 0
    neg = []
    res = []
    while(j<n):
        #Calculations
        if(arr[j] < 0):
            neg.append(arr[j])
        
        if(j-i+1 < k):
            j+=1
        elif(j-i+1 == k):
            #Ans
            if(len(neg) == 0):
                res.append(0)
            else:
                res.append(neg[0])
                if(arr[i] == neg[0]):
                    neg = neg[1:]
            i+=1
            j+=1
    print("First Negative Element in window size k is", res)
            

#Driver Code
arr = [9,-1,-7,3,-15,6,7,1]
n = len(arr)
k = 3
print(arr)
firstNegInWindowSizeK(arr, n , k)