# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"


#Functions
def decodedString(s):
    stack = []
    for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            substring = ""
            while stack[-1] != '[':
                substring = stack.pop() + substring
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = k + stack.pop()
            
            stack.append(int(k) * substring)
    return "".join(stack)
#Driver Code
s = "3[a2[c]]"
print("The decoded string is: ", decodedString(s))