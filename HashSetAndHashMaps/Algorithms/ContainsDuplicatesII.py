# Solution using hash map
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for idx, num in enumerate(nums):
            if num in map:
                if idx - map[num] <= k:
                    return True
            map[num] = idx

        return False
