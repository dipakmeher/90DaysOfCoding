#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# 12345
#  2345
#   345
#    45
#     5

n = int(input("Enter n: "))
row = 1
while(row<=n):
    # Printing spaces
    space = row-1
    while(space):
        print(" ", end='')
        space = space - 1

    # Printing numbers
    col=1
    while(col<=n-row+1):
        print(row+col-1,end='')
        col = col + 1
    print()
    row = row + 1

# Output:
# Enter n: 5
# 12345
#  2345
#   345
#    45
#     5