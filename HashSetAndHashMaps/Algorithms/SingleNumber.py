# Solution using a hashset to get rid of the duplicates
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
            else:
                hash_set.add(num)

        return hash_set.pop()
