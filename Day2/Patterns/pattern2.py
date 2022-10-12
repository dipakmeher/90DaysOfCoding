#Program to print the following pattern
# 1  1  1  1  1  
# 2  2  2  2  2
# 3  3  3  3  3
# 4  4  4  4  4
# 5  5  5  5  5

n = int(input("Enter n: "))
i = 0
while(i<n):
    j=0
    while(j<n):
        print(i+1," ",end='')
        j = j+1
    print()
    i = i + 1

# Output:
# Enter n: 5
# Enter n: 5
# 1  1  1  1  1  
# 2  2  2  2  2
# 3  3  3  3  3
# 4  4  4  4  4
# 5  5  5  5  5
