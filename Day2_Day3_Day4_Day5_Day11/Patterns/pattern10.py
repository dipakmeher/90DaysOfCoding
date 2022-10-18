#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# A  A  A  A  A  
# B  B  B  B  B  
# C  C  C  C  C  
# D  D  D  D  D  
# E  E  E  E  E

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
# A  A  A  A  A  
# B  B  B  B  B  
# C  C  C  C  C  
# D  D  D  D  D  
# E  E  E  E  E