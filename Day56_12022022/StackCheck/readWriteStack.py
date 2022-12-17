# while (there are more characters in the word to read) {
# 	read a character
# 	push the character on the stack
# }
# while (the stack is not empty) {
# 	write the stack's top character to the screen
# 	pop a character off the stack
# }
# What is written to the screen for the input "carpets"? 

str = "carpets"
stack = []
whileIndex = len(str)-1
index = 0
while(whileIndex >= 0):
    stack.append(str[index])
    index = index + 1
    whileIndex = whileIndex - 1

print("Stack = ",stack)
while(stack):
    print(stack.pop(), end=" ")

