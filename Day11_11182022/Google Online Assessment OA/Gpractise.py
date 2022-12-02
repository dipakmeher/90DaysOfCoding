A = [5,4,3,6,1]
res = [[A[0]]]
rowsCount = 0
for studHeight in A[1:]:
    key = studHeight
    flag = False
    for row in res:
        if key < row[-1]:
            row.append(key)
            flag = True
            break
    if not flag:
        res.append([key])
    
print("rowsCount = ",len(res))