#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
# A  B  C  D  E  
# B  C  D  E  F
# C  D  E  F  G
# D  E  F  G  H
# E  F  G  H  I

n = int(input("Enter n: "))
row = 1
while(row<=n):
    col=1
    while(col<=n):
        #ord function converts string into ASCII and chr function converts ASCII into string
        ch = chr(ord('A') + row -1 + col -1) 
        print(ch," ",end='')
        col = col + 1
    print()
    row = row + 1

# Output:
# Enter n: 5
# A  B  C  D  E  
# B  C  D  E  F
# C  D  E  F  G
# D  E  F  G  H
# E  F  G  H  I