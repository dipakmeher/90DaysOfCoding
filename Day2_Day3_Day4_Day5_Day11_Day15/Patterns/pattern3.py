#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# 1  2  3  4  5  
# 1  2  3  4  5  
# 1  2  3  4  5  
# 1  2  3  4  5  
# 1  2  3  4  5  

n = int(input("Enter n: "))
i = 0
while(i<n):
    j=0
    while(j<n):
        print(j+1," ",end='')
        j = j+1
    print()
    i = i + 1

# Output:
# Enter n: 5
# 1  2  3  4  5  
# 1  2  3  4  5  
# 1  2  3  4  5  
# 1  2  3  4  5  
# 1  2  3  4  5  