# Program to find the sum of even numbers
n = input("Enter n: ")
sum = 0
i=0
while i<=int(n):
    if(i%2 == 0):
        print(i," is Prime!")
        # Here, if use sum variable to print the values of sum then it will print the updated value of sum 
        #even after printing it before sum statement. It might be due to scope of sum variable being referred 
        # during the program which is same for all the appearance of sum variable in the program.
        # That's the reason we are temporarily storing an old sum in tempSum variable to print it.
        tempSum = sum
        print("Sum is ",i,"+",tempSum," = ", end='')
        sum = sum + i
        print(sum)
        print()
    i = i + 1
print("Sum of even numbers till ", n," is ", sum)