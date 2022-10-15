#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
    # Enter n: 5
    # 1  
    # 2  3
    # 3  4  5
    # 4  5  6  7
    # 5  6  7  8  9

n = int(input("Enter n: "))
row = 1
while(row<=n):
    col=1

    while(col<=n):
        #ord function converts string into ASCII and chr function converts ASCII into string
        ch = chr(ord('A') + row - 1) 
        print(ch," ",end='')
        col = col+1
    print()
    row = row + 1

# Output:
# Enter n: 5
# 1  
# 2  3
# 3  4  5
# 4  5  6  7
# 5  6  7  8  9