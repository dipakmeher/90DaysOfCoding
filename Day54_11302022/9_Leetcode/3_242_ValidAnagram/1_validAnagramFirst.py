# Input: s = "anagram", t = "nagaram"
# Output: true

def validAnagram(s,t):
    s1 = list(s)
    t1 = list(t)
    if(len(s1) != len(t1)):
        return False
    for i in t1:
        if i not in s1:
            return False
        s1.remove(i)
    return True


#Driver Code
# s = "anagram"
# t = "nagaram"
# s = "rat"
# t = "car"
s = "aacc"
t = "cacc"
print(validAnagram(s,t))