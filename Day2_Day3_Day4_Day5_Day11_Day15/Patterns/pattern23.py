#Love Babbar: Lecture 4 Solving pattern question
#Print the pattern in this format
# Enter n: 5
#     1
#    121
#   12321
#  1234321
# 123454321

n = int(input("Enter n: "))
row = 1
while(row<=n):
    # Printing first triangle: Number Triangle
    first = 1
    while(first<= n - row + 1):
        print(first, end='')
        first = first + 1

    # Printing Second Tirangle: Star first Triangle
    starFirst= row - 1
    while(starFirst):
        print("*",end='')
        starFirst = starFirst - 1

    # Printing Third Tirangle: Star sescond Triangle
    starSecond= row -1
    while(starSecond):
        print("*",end='')
        starSecond = starSecond - 1

    # Printing Fourth Tirangle: Number triangle
    numberSecond = n - row + 1
    while(numberSecond):
        print(numberSecond, end='')
        numberSecond = numberSecond - 1
    print()
    row = row + 1

# Output:
# Enter n: 5
#     1
#    121
#   12321
#  1234321
# 123454321