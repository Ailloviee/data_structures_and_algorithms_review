# Solution using a hash set to detect a 'cycle' in the calculation
class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()

        sum = 0
        while sum != 1:
            sum = 0

            while n != 0:
                sum += (n % 10) ** 2
                n = n // 10

            if sum in num_set:
                return False
            else:
                num_set.add(sum)
            n = sum

        return True
