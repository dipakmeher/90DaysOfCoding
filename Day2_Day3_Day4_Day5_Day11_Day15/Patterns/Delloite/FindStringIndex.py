# Find the index of the digits present in string
# input: "012ABDH52"; Output: 01278

s = "012ABDH52"
res = ""
for i in range(len(s)):
    if(s[i]>='0' and s[i]<="9"):
        res = res + str(i)
print("Index of the digits in String: ",res)

#Output: 
# Index of the digits in String:  01278