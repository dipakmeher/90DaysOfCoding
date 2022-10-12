#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 3
# 1  2  3  
# 4  5  6
# 7  8  9

n = int(input("Enter n: "))
i = 0
count = 1
while(i<n):
    j=0
    while(j<n):
        print(count," ",end='')
        count+=1
        j = j+1
    print()
    i = i + 1

# Output:
# Enter n: 3
# 1  2  3  
# 4  5  6
# 7  8  9