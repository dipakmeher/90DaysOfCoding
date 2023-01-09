#input digit = "23"
#Asked: Find out the possible number of subsets from the string given on keypad
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#Function
def LetterCombinationOfNumber(ip,op):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    countAlpha = 0
    keypad = dict()
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
        print(alphabets)
        #a[:3] 0-2 ck 3 ca 3,a[:6] 

        

    print(keypad)
#Driver Code
ip = "23"
op=""
res = []
LetterCombinationOfNumber(ip,op)
print("Total possible subsets are: ", res)