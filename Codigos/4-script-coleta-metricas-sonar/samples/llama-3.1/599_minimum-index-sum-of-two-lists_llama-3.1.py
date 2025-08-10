class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        dic1 = {restaurant:i for i, restaurant in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for i, restaurant in enumerate(list2):
            if restaurant in dic1:
                index_sum = dic1[restaurant] + i
                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [restaurant]
                elif index_sum == min_sum:
                    result.append(restaurant)
        return result