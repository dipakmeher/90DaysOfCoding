#Minimum number of flips required to achieve equal number of heads-0 and tails- 1
# The code was working fine without numpy array. In CA, in python, the array would be list only
import numpy as np
Z = [1,0,0,1,0,0]
#A = [int(i) for i in Z]
A = np.array([1,0,0,1,0,0])

print("A Type",type(A))
#A = [1,1,0,1]
li =  A.tolist()
print("Li Type",type(A))
head = li.count("0") 
tail = li.count("1")
res = abs(head-tail)

print(res/2)