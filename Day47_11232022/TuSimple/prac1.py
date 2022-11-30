# https://leetcode.com/problems/combination-sum-iii/
tempList = []
result = [] 
def CreateCombinations(start, k, n):
    print("k = ",k)
    print("n = ",n)
    if(k<0 or n<0):
        print("List Returned.")
        return
    if(k==0 and n==0):
        print("templist = ", tempList)
        result.append(tempList)
        print("List Added. ")
        return
    for i in range(start,10):
        tempList.append(i)
        # print("templist = ", tempList)
        CreateCombinations(i+1, k-1, n-i)
        tempList.pop()
    return


# def Solutions(k, n):
k = 3
n = 9
CreateCombinations(1,k,n)
print("Result= ", result)


    # return result

# if __name__ == "__main__":
#     k = 3
#     n = 9
#     print("Solution: ", Solutions(k, n))

# Expected Output: Output: [[1,2,6],[1,3,5],[2,3,4]] 