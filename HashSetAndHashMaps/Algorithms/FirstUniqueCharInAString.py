from collections import defaultdict

# Solution using a hashmap to store occurences of a char in the string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c_map = defaultdict(int)
        for c in s:
            c_map[c] += 1

        for c in s:
            if c_map[c] == 1:
                return s.index(c)

        return -1
