class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for str in strs:
            ss = sorted(str)
            res["".join(ss)].append(str)

        return res.values()
