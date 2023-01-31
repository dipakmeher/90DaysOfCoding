import heapq
records = [
    "Even: 1", 
    "Erik: 2",
    "Even: 2",
    "Even: 5",
    "Erik: 3",
    "Erik: 4",
    "A: 1",
    "T: 1",
    "Erik: 2",
    "Erik: 2",
    "Even: 3",
    "Erik: 5",
    "T: 2",
    "Even: 4",
    "T: 1",
    "Erik: 2",
    "A: 4",
    "Even: 3",
    "Erik: 3",
    "A: 2"
]
temp = dict()
maxavg = -1
res = ""
heap = []
for rec in records:
    if rec[:-3] in temp:
        tempLst = temp[rec[:-3]]
        total = tempLst[0]
        count = tempLst[1]
        avg = tempLst[-1]
        total += int(rec[-1])
        count += 1
        avg = total/count
        tempLst[0] = total
        tempLst[1] = count
        tempLst[-1] = avg
        temp[rec[:-3]] = tempLst
        print(rec[:-3])
        print("maxavg<<>>avg",maxavg, avg)
        heapq.heappush(heap,[-avg, rec[:-3]])
        if(maxavg < avg):
            maxavg = avg
            res = rec[:-3]
            print("res = ",res)
        #heap.append([-avg, rec[:-3]])
        print("when present",temp)
    else:
        tempLst = []
        total = int(rec[-1])
        count = 1
        avg = total/count
        tempLst.append(total)
        tempLst.append(count)
        tempLst.append(avg)
        temp[rec[:-3]] = tempLst
        heapq.heappush(heap,[-avg, rec[:-3]])
        if(maxavg < avg):
            maxavg = avg
            res = rec[:-3]
            print("res = ",res)
        print("when not present",temp)
    print()
print("temp = ",temp)
print(res)
print()
print(heap)
print(heap[0][-1])