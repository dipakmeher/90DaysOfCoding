# Input: s = "anagram", t = "nagaram"
# Output: true

def validAnagram(s,t):
    for letter in s:
        if s.count(letter) != t.count(letter):
            return False
        return set(s) == set(t) and len(s) == len(t)


#Driver Code
s = "aacc"
t = "cacc"
print(validAnagram(s,t))