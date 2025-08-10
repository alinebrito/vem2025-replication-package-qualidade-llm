class Solution:
    def findUnsortedSubarray(self, N: List[int]) -> int:
        lenN, left, right = len(N) - 1, -1, -1
        min_unsorted, max_unsorted = float('inf'), float('-inf')
        
        for i in range(len(N)):
            if i > 0 and N[i] < N[i - 1]:
                right = i
            if i < len(N) - 1 and N[lenN - i] > N[lenN - i - 1]:
                left = lenN - i - 1
        
        if left == -1:
            return 0
        
        for i in range(left, right + 1):
            min_unsorted = min(min_unsorted, N[i])
            max_unsorted = max(max_unsorted, N[i])
        
        while left > 0 and N[left - 1] > min_unsorted:
            left -= 1
        while right < lenN and N[right + 1] < max_unsorted:
            right += 1
        
        return right - left + 1