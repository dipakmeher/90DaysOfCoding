# Count characters in each words in the given string
#input: " India is my Country"; Output: 5 2 2 7

s = " India is my Country "
for z in s.split():
    print(len(z)," ",end="")
