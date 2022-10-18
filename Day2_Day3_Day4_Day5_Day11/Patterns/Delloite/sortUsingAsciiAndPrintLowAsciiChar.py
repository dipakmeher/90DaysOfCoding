# Print the lowest ascii value for the count =  count of character with a highest Ascii value

s = "ABOVEtheheight"
charS = list(s)

asciiCharS = [ord(i) for i in charS]

charS.sort()
asciiCharS.sort()

print(charS)
print(asciiCharS)

count = 0
for i in asciiCharS:
    if(asciiCharS[-1]==i):
        count+=1
print("Count of highest ASCII value: ", count)
for z in range(count):
    print(charS[0])



