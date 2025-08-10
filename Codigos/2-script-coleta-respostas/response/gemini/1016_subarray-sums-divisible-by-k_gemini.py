class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        dic = {0: 1}
        for i in range(len(nums)):
            sums += nums[i]
            rem = sums % k
            if rem in dic:
                count += dic[rem]
            dic[rem] = dic.get(rem, 0) + 1
        return count