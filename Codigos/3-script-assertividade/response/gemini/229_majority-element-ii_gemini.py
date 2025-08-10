class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)
        if nums.count(candidate2) > len(nums) // 3 and candidate1 != candidate2:
            result.append(candidate2)
        return result