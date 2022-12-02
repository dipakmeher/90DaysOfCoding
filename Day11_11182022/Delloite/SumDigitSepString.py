# Find the sum of the numbers present in String and print String and syn separately
#input: "2018 India is 18 my country"
# Output: 
# Indiaismycountry 
# 2036

s = "2018 India is 18 my country"
stringOnly = ""
numberSum = 0

for z in s.split():
    if z.isdigit():
        numberSum = numberSum + int(z)
    else:
        stringOnly = stringOnly + z

print("stringOnly in String: ",stringOnly)
print("numberSum in String: ",numberSum)

# stringOnly in String:  Indiaismycountry
# numberSum in String:  2036