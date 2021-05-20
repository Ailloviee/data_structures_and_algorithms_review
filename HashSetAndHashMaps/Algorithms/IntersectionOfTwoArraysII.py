from collections import defaultdict

# Solution using two hash maps to store occurences of characters of two strings and get min of each to match intersection
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for num in nums1:
            map1[num] += 1
        for num in nums2:
            map2[num] += 1

        res = []
        for num in map1:
            if num in map2:
                for _ in range(min(map1[num], map2[num])):
                    res.append(num)

        return res
