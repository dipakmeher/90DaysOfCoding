# Input: s = "anagram", t = "nagaram"
# Output: true

def validAnagram(s,t):
    if(len(s) == 0 and len(t) == 0):
        return True
    for letter in s:
        if s.count(letter) != t.count(letter):
            return False
        return set(s) == set(t) and len(s) == len(t)


#Driver Code
s = "aacc"
t = "cacc"

s = "compilations"
t = "complainants"
print(s.count('n'))
print(t.count('n'))

# s = ""
# t = ""
print(validAnagram(s,t))