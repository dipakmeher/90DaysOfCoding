#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# E  
# D  E
# C  D  E
# B  C  D  E
# A  B  C  D  E 

n = int(input("Enter n: "))
row = 1
while(row<=n):
    col=1
    # For Printing Triangle, run the loop till row
    while(col<=row):
        #ord function converts string into ASCII and chr function converts ASCII into string
        ch = chr(ord('A') + n - row + col -1) 
        print(ch," ",end='')
        col = col + 1
    print()
    row = row + 1

# Output:
# Enter n: 5
# E  
# D  E
# C  D  E
# B  C  D  E
# A  B  C  D  E