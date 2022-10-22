#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 4
#    1
#   23
#  456
# 78910

n = int(input("Enter n: "))
row = 1
start = 1
while(row<=n):
    # Printing spaces
    space = n - row
    while(space):
        print(" ", end='')
        space = space - 1

    # Printing numbers
    col=1
     # For Printing Triangle, run the loop till row
    while(col<=row):
        print(start,end='')
        start = start + 1
        col = col + 1
    print()
    row = row + 1

# Output:
# Enter n: 4
#    1
#   23
#  456
# 78910