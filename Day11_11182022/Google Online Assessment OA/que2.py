# Total insertion required to convert a string into a format abcabcabc
# Function
def insertionTotal(s,n,count,last):
    i = 0
    currentChar = ""
    while(i<n):
        currentChar = s[i]
        if (last == "c" and currentChar != "a") :
            last = "a"
            count+=1
        elif(last == "a" and currentChar != "b"):
            last = "b"
            count+=1
        elif(last == "b" and currentChar != "c"):
            last = "c"
            count+=1
        else:
            last = currentChar
            i+=1
    return count
        
#Driver Code   
s = "aabcc"
n = len(s)
count = 0
last = "c"
print("Total insertion required ", insertionTotal(s,n,count,last))