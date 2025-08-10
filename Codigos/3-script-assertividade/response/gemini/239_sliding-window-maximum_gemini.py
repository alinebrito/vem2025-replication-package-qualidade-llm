class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        deq = deque()
        max_idx = 0
        for i in range(k):
            self.clean_deque(nums, k, i, deq)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        for i in range(k, n):
            self.clean_deque(nums, k, i, deq)
            deq.append(i)
            output.append(nums[deq[0]])
        
        return output
    
    def clean_deque(self, nums, k, i, deq):
        if deq and deq[0] == i - k:
            deq.popleft()
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()