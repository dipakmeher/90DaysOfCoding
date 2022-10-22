#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
#     1
#    121
#   12321
#  1234321
# 123454321

n = int(input("Enter n: "))
row = 1
while(row<=n):
    # Printing space triangle
    space = n - row
    while(space):
        print(" ", end='')
        space = space - 1

    # Printing Second Tirangle
    col=1
     # For Printing Triangle, run the loop till row
    while(col<=row):
        print(col,end='')
        col = col + 1

    # Printing Third Tirangle
    start = row - 1
    while(start):
        print(start, end='')
        start = start - 1
    print()
    row = row + 1

# Output:
# Enter n: 5
#     1
#    121
#   12321
#  1234321
# 123454321