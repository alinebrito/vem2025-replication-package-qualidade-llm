class Solution(object):
    def maxProduct(self, nums):
        max_product = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product = (nums[i]-1)*(nums[j]-1)
                    max_product = max(max_product, product)
        return max_product