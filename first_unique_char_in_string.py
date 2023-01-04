# Problem : Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        st_map = {}
        for i in range (0, len(s)):
            if s[i] not in st_map:
                st_map[s[i]] = True
            else:
                st_map[s[i]] = False

        for i in range (0, len(s)):
            if st_map[s[i]]:
                return i 
        return -1


# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2
