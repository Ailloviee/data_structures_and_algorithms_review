from collections import defaultdict

# Solution using DP
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count_sums = {}
        count_sums[0] = 1

        for num in nums:
            temp = defaultdict(int)
            for sum, val in count_sums.items():
                temp[sum + num] += val
                temp[sum - num] += val
            count_sums = temp

        return count_sums[target]
