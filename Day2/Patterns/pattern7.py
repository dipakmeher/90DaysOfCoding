#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 3
# 1  2  3  
# 4  5  6
# 7  8  9

n = int(input("Enter n: "))
row = 0
count = 1
while(row<n):
    col=0
    while(col<=row):
        print(count," ",end='')
        count+=1
        col = col+1
    print()
    row = row + 1

# Output:
# Enter n: 3
# 1  2  3  
# 4  5  6
# 7  8  9