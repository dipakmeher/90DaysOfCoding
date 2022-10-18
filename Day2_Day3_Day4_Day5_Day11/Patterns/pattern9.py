#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# 1  
# 2  1
# 3  2  1
# 4  3  2  1
# 5  4  3  2  1

n = int(input("Enter n: "))
row = 1
while(row<=n):
    col=1
    while(col<=row):
        print(row - col + 1," ",end='')
        col = col+1
    print()
    row = row + 1

# Output:
# Enter n: 5
# 1  
# 2  1
# 3  2  1
# 4  3  2  1
# 5  4  3  2  1