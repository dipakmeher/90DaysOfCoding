#Valid Parenthesis Leetcode
 # stack = ([])
    # index = )
    # if stack == 
def validParen(str):
    if(len(str) == 0):
        return None
    stack = []
    for i in range(len(str)):
        if(str[i] == "(" or str[i] == "[" or str[i] == "{"):
            stack.append(str[i])
            continue
        if(len(stack) == 0):
            return False
        if(str[i] == ")"):
            if(stack[-1] == "("):
                stack.pop()
            else:
                return False
        elif(str[i] == "]"):
            if(stack[-1] == "["):
                stack.pop()
            else:
                return False
        elif(str[i] == "}"):
            if(stack[-1] == "{"):
                stack.pop()
            else:
                return False
        
    if(len(stack) == 0):
        return True
    else:
        return False
         

#Driver Code
str = "{]}"
print("The string str is,",validParen(str))



# for i in range(len(str)):
#     if(str[i] == "(" or str[i] == "[" or str[i] == "{"):
#         if str[i] in heap:
#             heap[str[i]] += 1
#         else:
#             heap[str[i]] = 1
   
#     if(str[i] == ")"):
#         heap["("]-=1
#         print("(", heap["("])
#         if(heap["("]==0):
#             del heap["("]
    
#     if(str[i] == "]"):
#         heap["["]-=1
#         if(heap["["]==0):
#             del heap["["]

#     if(str[i] == "}"):
#         heap["{"]-=1
#         if(heap["{"]==0):
#             del heap["{"]
    
# if(len(heap) > 0):
#     print("False")
# else:
#     print("True")