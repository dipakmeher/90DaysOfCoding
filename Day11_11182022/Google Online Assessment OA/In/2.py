def secondInterview(parse_log):
    timeStamp = []
    for rec in parse_log:
        timeStamp.append(rec[1])
        timeStamp.append(rec[2])
    timeStamp.sort()
    print(timeStamp)

    stack = []
    for i in range(1,len(timeStamp)):
        temp = []
        temp.append(timeStamp[i-1])
        temp.append(timeStamp[i])
        for rec in parse_log:
            if rec[1]<=timeStamp[i-1] and timeStamp[i]<=rec[2]: # Error
                # A: 1>=1 and 5<=10
                # B: 5<=1 and 
                temp.append(rec[0])
        stack.append(temp)
    return stack

#Driver Code
parse_log = [("A", 1, 10), ("B", 5,7), ("C",6,12), ("D", 15, 17)]
print(secondInterview(parse_log))