#input digit = "23"
#Asked: Find out the possible number of subsets from the string given on keypad
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#For two strings we can do using recursion but for more than two strings Recursion is difficult to implement
#Following is for two string
#Function

def LCRecursion(ip,op):
    if(len(op) == 2):
        res.append(op)
        return
    if(len(ip) == 0):
        return
    
    op1 = op + ip[0]
    op2 = op

    LCRecursion(ip[1:],op1)
    LCRecursion(ip[1:],op2)

def LetterCombinationOfNumber(ip,op):
    first = keypad[ip[0]]
    second = keypad[ip[1]]
    ip = second
    op = ""
    for i in first:
        op = op + i
        print(op)
        LCRecursion(ip, op)
        op = ""
    print(keypad)
def makeKeypad(ip,op):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    countAlpha = 0
    while(len(ip) != 0):
        countKeypad = ip[0]
        if(countKeypad == 7 or countKeypad == 9):
            keypad[countKeypad] = alphabets[:countAlpha + 4]
            alphabets = alphabets[countAlpha + 4:]
            ip = ip[1:]
            continue
        keypad[countKeypad] = alphabets[:countAlpha + 3]
        alphabets = alphabets[countAlpha + 3:]
        ip = ip[1:]
        #a[:3] 0-2 ck 3 ca 3,a[:6] 
#Driver Code
ip = "23"
op=""
res = []
keypad = dict()

makeKeypad(ip,op)
LetterCombinationOfNumber(ip,op)
print("Total possible subsets are: ", res)