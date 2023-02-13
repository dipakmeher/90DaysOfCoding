# Input: x = 123
# Output: 321

#Function
def reverseInteger(x):
    temp = ""
    if x<0:
        temp = "n"
    rev = list(str(abs(x)))
    rev.reverse()

    v = int("".join(i for i in rev))
    if( temp == "n"):
        v = -v
    if(v>=(-2**31) and v<=(2**31)-1):
        return v
    return 0

#Driver Code
x = -123
print(reverseInteger(x))