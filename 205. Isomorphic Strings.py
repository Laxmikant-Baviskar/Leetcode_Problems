# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# ==========================================
# s = "party"
# t = "theer"
# s = "egg"
# t = "add"
s = "paper"
t = "title"

i = 0
co1=[]
co2=[]
if len(s) == len(t):
    for i in s:
        c1 = s.count(i)
        co1.append(c1)
        print(co1)
        # print("---------")
    for i in t:
        c2 = t.count(i)
        co2.append(c2)
        print(co2)
else :
    print("size not match")

if co1 == co2:
    print("True") 
else:
    print("False")
# ==========================================


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return len(set(s))==len(set(zip(s,t)))==len(set(t))



# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true