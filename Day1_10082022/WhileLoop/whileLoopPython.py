i = 1
sum = 0
while i<6:
    # if i == 3:
    #     i = i + 1
    #     continue #Continue Statement
    # if i == 4:
    #     i = i + 1
    #     break #Continue Statement

    sum = sum + i
    print("Sum is ", sum) # When the code was just after commented break stmt, indentation error was there. But now it is running fine. 
    i = i + 1
else:
    print("i >=6 now!")

# Output
# Sum is  1
# Sum is  3
# Sum is  6
# Sum is  10
# Sum is  15
# i >=6 now!
