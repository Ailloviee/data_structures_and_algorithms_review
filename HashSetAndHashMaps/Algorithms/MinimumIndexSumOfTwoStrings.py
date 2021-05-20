# Solution using a hashmap to store one of the list's index based on string value
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        min_sum = float("inf")
        list1_map = {}
        for idx, name in enumerate(list1):
            list1_map[name] = idx

        for idx, name in enumerate(list2):
            if name in list1_map:
                new_sum = idx + list1_map[name]
                if new_sum < min_sum:
                    min_sum = new_sum
                    res = [name]
                elif new_sum == min_sum:
                    res.append(name)

        return res

