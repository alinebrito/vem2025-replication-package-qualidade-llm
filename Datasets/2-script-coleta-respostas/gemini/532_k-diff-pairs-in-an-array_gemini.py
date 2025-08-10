class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt=0
        seen = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j]) == k and (nums[i],nums[j]) not in seen:
                    cnt+=1
                    seen.add((nums[i],nums[j]))
                    seen.add((nums[j],nums[i]))
        return cnt