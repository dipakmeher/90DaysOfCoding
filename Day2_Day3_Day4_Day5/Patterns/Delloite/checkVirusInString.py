# Virus is present in a string if the alternate character in string are same.
# input: "ADAOAS"; Output: Virus is there

s = "ADAOCS"
k = s[0]
flag = 1
for i in range(0,len(s),+2):
    if(s[i]!=k):
        flag = 0;
        break
if(flag == 0):
    print("Virus is not present...")
else:
    print("Virus is present")