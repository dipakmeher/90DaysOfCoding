symbols = "TTFT"
operator = "|&^"

x = len(symbols)
y = len(operator)
arr = ""
i=0
j = 0
while i < x and j < y:
    arr += symbols[i]+operator[j]
    i+=1
    j+=1
while i < x:
    arr += symbols[i]
    i+=1
while j < y:
    arr += operator[j]
    j+=1
    
print(arr)
print(0+False)