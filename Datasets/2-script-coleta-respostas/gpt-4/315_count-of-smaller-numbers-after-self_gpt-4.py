class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            if len(enum) <= 1:
                return enum
            mid = len(enum) // 2
            left = sort(enum[:mid])
            right = sort(enum[mid:])
            i = j = 0
            counts = [0] * len(enum)
            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    counts[left[i][0]] += len(right) - j
                    i += 1
                else:
                    j += 1
            return left + right

        indexed_nums = [(i, nums[i]) for i in range(len(nums))]
        sort(indexed_nums)
        return [counts[i] for i in range(len(nums))]