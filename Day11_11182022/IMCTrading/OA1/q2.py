# 12/15 Test Cases Passed

from collections import deque

def getResult(arrival, direction):
    
    time = 0
    i = 0
    prev_hiker = 1
    q1, q0 = deque(), deque()
    res = [0] * len(arrival)
    
    while True:
        move = True
        
        while i < len(arrival) and arrival[i] == time:
            if direction[i] == 0:
                q0.append(i)
            else:
                q1.append(i)
            i += 1
    
        if q0 and not q1:
            prev_hiker = 0
    
        while prev_hiker == 1 and q1:
            res[q1.popleft()] = time
            time += 1
            move = False
            while i < len(arrival) and arrival[i] == time:
                if direction[i] == 0:
                    q0.append(i)
                else:
                    q1.append(i)
                i += 1

        while prev_hiker == 0 and q0:
            res[q0.popleft()] = time
            time += 1
            move = False
            while i < len(arrival) and arrival[i] == time:
                if direction[i] == 0:
                    q0.append(i)
                else:
                    q1.append(i)
                i += 1

        if not q0:
            prev_hiker = 1

        if move:
            time = arrival[i]
            continue

        if not q0 and not q1 and i == len(arrival):
            return res

print(getResult([0,0,1,4], [0,1,1,0]))