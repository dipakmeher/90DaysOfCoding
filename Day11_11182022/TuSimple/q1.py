# Question send by Dhruval   

red = [2,3,4]
blue = [3,1,1]
bluecost = 2

res = [0]
R=0
B=0

R1=0
B1=0
flag = "Z"


for i in range(0, len(red)):

    if(red[i]>blue[i])
    if(flag == "B"):
        R = R+ red[i]
        B = B + blue[i]

        S1 = B + red[i] 
    else:
        R = R+ red[i]
        B = B+ bluecost + blue[i]

        S1 = R + bluecost + blue[i]

    if(R==B):
        flag = B
        res.append(B)
    elif(R<B):
        flag = R
        res.append(R)
    else:
        flag = B
        res.append(B)
    

print("Result: ",res)