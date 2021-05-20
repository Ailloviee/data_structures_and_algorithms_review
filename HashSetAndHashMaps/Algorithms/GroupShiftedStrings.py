# Solution using a hashmap to store strings that have the same intervals
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for string in strings:
            if len(string) == 1:
                res["0"].append(string)
            else:
                key = ""
                for i in range(1, len(string)):
                    key += str((ord(string[i]) - ord(string[i - 1])) % 26)
                    key += ","
                res[key].append(string)

        return res.values()
