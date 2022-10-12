#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# 1  
# 1  2
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5

n = int(input("Enter n: "))
row = 1
while(row<=n):
    col=1
    while(col<=row):
        print(col," ",end='')
        col = col+1
    print()
    row = row + 1

# Output:
    # Enter n: 5
    # 1  
    # 1  2
    # 1  2  3
    # 1  2  3  4
    # 1  2  3  4  5