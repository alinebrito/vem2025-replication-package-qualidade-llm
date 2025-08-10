class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, current):
            max_length = len(current)
            for i in range(index, len(arr)):
                new_string = current + arr[i]
                if len(set(new_string)) == len(new_string):
                    max_length = max(max_length, backtrack(i + 1, new_string))
            return max_length
        
        return backtrack(0, "")