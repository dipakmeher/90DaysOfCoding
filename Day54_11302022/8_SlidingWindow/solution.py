def solution(l, t):
    # Your code here
    i=0
    j=0
    ans = []
    sum = 0
    while(j<len(l)):
        sum = sum + l[j]
        if(sum<t):
            j+=1
        elif(sum==t):
            ans.append([i,j])
            sum = sum - l[i]
            j+=1
        elif(sum>t):
            while sum > t:
                sum = sum - l[i]
                i+=1
            j+=1
    if len(ans) ==0:
        ans.append([-1,-1])
        return ans[0]
    return ans[0]

l = [4,3,10,2,8]
t = 12
print(solution(l,t))