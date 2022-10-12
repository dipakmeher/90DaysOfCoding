#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# 5  4  3  2  1  
# 5  4  3  2  1
# 5  4  3  2  1
# 5  4  3  2  1
# 5  4  3  2  1

n = int(input("Enter n: "))
i = 0
while(i<n):
    j=0
    while(j<n):
        print(n-j," ",end='')
        j = j+1
    print()
    i = i + 1

# Output:
# Enter n: 5
# 5  4  3  2  1  
# 5  4  3  2  1
# 5  4  3  2  1
# 5  4  3  2  1
# 5  4  3  2  1 