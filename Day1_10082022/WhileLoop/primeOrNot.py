n = int(input("Enter n: "))
i=2 # Starting from 2 because Prime number will be divisible by 1 or itself
count = 0
while(i<n):
    if(n%i == 0):
        count+=1
        break
    i+=1
if(count == 0):
    print(n, " is prime!")
else:
    print(n," is not prime!")
    
    

