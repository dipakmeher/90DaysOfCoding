#Program to print the following pattern
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = int(input("Enter n: "))
i = 0
while(i<n):
    j=0
    while(j<n):
        print("* ",end='')
        j = j+1
    print()
    i = i + 1

# Output:
# Enter n: 5
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
