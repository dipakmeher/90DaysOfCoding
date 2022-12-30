#Tower of Hanoi: Recursion 
#Function 
def TOH(source, destination, helper, n):
    global count
    count = count + 1
    if(n==1):
        print("Move 1 disk from,",source,"to",destination)
        return

    TOH(source,helper,destination,n-1)
    print("Move 1 disk from,",source,"to",destination)
    TOH(helper,destination,source,n-1)

#Driver code
n = 3
count = 0
TOH('s','d','h', n)
print("Not of shifts required to move the disks from source to destination:", count)