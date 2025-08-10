class Solution:
    def reversePairs(self, nums):
        def merge_sort(arr):
            if len(arr) < 2:
                return arr, 0  
            mid = len(arr) // 2  
            left, left_count = merge_sort(arr[:mid])
            right, right_count = merge_sort(arr[mid:])
            count = left_count + right_count
            
            j = 0  
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1  
                count += j
            
            merged = sorted(left + right)
            return merged, count

        _, total_count = merge_sort(nums)
        return total_count  