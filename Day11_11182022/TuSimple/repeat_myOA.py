# Incomplete Code. 
import math
word = "abaaaaa"
ls = list(word)
a = ls.count('a') 
b = ls.count('b')
c = ls.count('c')

# a1 = (a-1)
# b1 = (b-1)
# c1 = (c-1)
x = 0
y = z = 0
# if(a>1):
#     x = math.floor(a/2)
# if(b>1):
#     y = math.floor(b/2)
# if(c>1):
#     z = math.floor(c/2)
if(a>1):
    if((a-1)%2 ==0 ):
        x = math.floor((a-1)/2)
    else:
        x = math.floor((a-1)/2) + 1
if(b>1):
    if((b-1)%2 ==0 ):
        y = math.floor((b-1)/2)
    else:
        y = math.floor((b-1)/2) + 1

if(c>1):
    if((c-1)%2 ==0 ):
        z = math.floor((c-1)/2)
    else:
        z = math.floor((c-1)/2) + 1

print(x+y+z)


