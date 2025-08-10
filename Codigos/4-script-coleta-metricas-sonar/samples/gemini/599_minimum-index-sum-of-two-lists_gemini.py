class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {restaurant:i for i, restaurant in enumerate(list1)}
        min_sum = float('inf')
        res = []
        for i, restaurant in enumerate(list2):
            if restaurant in dic1:
                curr_sum = i + dic1[restaurant]
                if  curr_sum < min_sum:
                    res = [restaurant]
                    min_sum = curr_sum
                elif curr_sum == min_sum:
                    res.append(restaurant)
        return res