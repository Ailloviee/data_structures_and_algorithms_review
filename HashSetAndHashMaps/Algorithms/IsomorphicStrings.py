# Solution using a hash map to match characters from one string to that of the other
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = {}
        mapped = {}

        N = len(s)

        for i in range(N):
            if s[i] not in iso:
                if t[i] in mapped:
                    return False
                else:
                    iso[s[i]] = t[i]
                    mapped[t[i]] = True
            else:
                if iso[s[i]] != t[i]:
                    return False

        return True
