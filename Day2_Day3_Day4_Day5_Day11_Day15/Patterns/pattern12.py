#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5 
# A  B  C  D  E  
# F  G  H  I  J
# K  L  M  N  O
# P  Q  R  S  T
# U  V  W  X  Y

n = int(input("Enter n: "))
row = 1
start = 0
while(row<=n):
    col=1
    while(col<=n):
        #ord function converts string into ASCII and chr function converts ASCII into string
        ch = chr(ord('A') + start) 
        print(ch," ",end='')
        start = start+1
        col = col + 1
    print()
    row = row + 1

# Output:
# Enter n: 5 
# A  B  C  D  E  
# F  G  H  I  J
# K  L  M  N  O
# P  Q  R  S  T
# U  V  W  X  Y