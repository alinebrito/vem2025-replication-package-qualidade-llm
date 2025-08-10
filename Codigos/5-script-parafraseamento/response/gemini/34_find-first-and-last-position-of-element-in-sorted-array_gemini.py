class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                res[0]=mid
                res[1]=mid
                i=mid-1
                while i>=0 and nums[i]==target:
                    res[0]=i
                    i-=1
                j=mid+1
                while j<len(nums) and nums[j]==target:
                    res[1]=j
                    j+=1
                return res
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return res