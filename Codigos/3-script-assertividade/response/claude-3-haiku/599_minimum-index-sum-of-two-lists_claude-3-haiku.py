class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {restaurant:i for i, restaurant in enumerate(list1)}
        min_sum = float('inf')
        result = []
        for j, restaurant in enumerate(list2):
            if restaurant in dic1:
                curr_sum = dic1[restaurant] + j
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [restaurant]
                elif curr_sum == min_sum:
                    result.append(restaurant)
        return result