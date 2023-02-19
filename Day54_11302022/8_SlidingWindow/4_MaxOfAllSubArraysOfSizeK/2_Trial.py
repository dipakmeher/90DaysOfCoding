#Functions
def maxOfAllSubArraysOfKSize(arr,n, k):
    i = 0
    j = 0
    mx = 0
    temp = []
    res = []
    while(j<n):
        # while(len(temp)>0 and temp[-1]<arr[j]): # We need to maintain list to store the required elements
        #     # Temp should be purpose based and thats why we need to pop the elements smaller that a[j]
        #     temp.pop(0)
        if(len(temp)>0 and temp[-1]<arr[j]): # cant do any modification
            temp.append(arr[j])

        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            if(len(temp)==0):
                res.append(0)
            else:
                res.append(temp[-1])
                if(arr[i] == temp[0]):
                    temp.pop(0)
            i+=1
            j+=1
    print("Maximum of all subarrays of size k",res)

#Driver Code
arr = [1,3,-1,-3,-5,8,9]
n = len(arr)
k = 3
print(arr)
maxOfAllSubArraysOfKSize(arr,n, k)
