# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Status: Best Solution
def Sum3(nums, n):
    res = set()
    n, p, z = [], [], []
    for num in nums:
        if num > 0: p.append(num)
        elif num < 0: n.append(num)
        else: z.append(num)
    N, P = set(n), set(p)
    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, num))
    if len(z) >= 3:
        res.add((0,0,0))
        if (not n and p) or (not n and not p) or (n and not p): return res 
    for i, a in enumerate(n):
        for b in n[i+1:]:
            target = -1*(a+b)
            if target in P:
                res.add(tuple(sorted([a,b,target])))
    for i, a in enumerate(p):
        for b in p[i+1:]:
            target = -1*(a+b)
            if target in N:
                res.add(tuple(sorted([a,b,target])))

    return res


#Drivers Code
nums = [-1,0,1,2,-1,-4]
n = len(nums)

print(Sum3(nums,n))

