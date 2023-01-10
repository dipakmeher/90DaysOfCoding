# Python3 implementation of the approach
from collections import deque

# Function to return a list that contains
# all the generated letter combinations


def letterCombinationsUtil(number, n, table):
    resList = []
    q = deque()
    q.append("")

    while(len(q) != 0):
        s = q.popleft()

        if(len(s)==n):
            resList.append(s)
        else:
            for letter in table[number[len(s)]]:
                q.append(s+letter)
    return resList


# Function that creates the mapping and
# calls letterCombinationsUtil
def letterCombinations(number, n):

	# table[i] stores all characters that
	# corresponds to ith digit in phone
	table = ["0", "1", "abc", "def", "ghi", "jkl",
			"mno", "pqrs", "tuv", "wxyz"]

	list = letterCombinationsUtil(number, n, table)

	s = ""
	for word in list:
		s += word + " "

	print(s)
	return


# Driver code
number = [2, 3,4,5]
n = len(number)

# Function call
letterCombinations(number, n)
