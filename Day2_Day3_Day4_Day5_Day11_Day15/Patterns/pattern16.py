#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
#     *
#    **
#   ***
#  ****
# ***** 

n = int(input("Enter n: "))
row = 1
while(row<=n):
    # Printing spaces
    space = n - row
    while(space):
        print(" ", end='')
        space = space - 1

    # Printing stars
    col=1
     # For Printing Triangle, run the loop till row
    while(col<=row):
        #ord function converts string into ASCII and chr function converts ASCII into string
        print("*",end='')
        col = col + 1
    print()
    row = row + 1

# Output:
# Enter n: 5
#     *
#    **
#   ***
#  ****
# *****