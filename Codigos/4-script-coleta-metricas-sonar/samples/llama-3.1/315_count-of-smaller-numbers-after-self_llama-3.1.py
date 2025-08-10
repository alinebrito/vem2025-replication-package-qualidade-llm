class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            if len(enum) <= 1:
                return enum
            mid = len(enum) // 2
            left = sort(enum[:mid])
            right = sort(enum[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i, j = 0, 0
            count = 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    count += len(left) - i
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result, count

        enum = [(v, i) for i, v in enumerate(nums)]
        enum, _ = sort(enum)
        counts = [0] * len(nums)
        for i, (v, j) in enumerate(enum):
            if i < len(enum) - 1 and v < enum[i + 1][0]:
                counts[j] = len(enum) - i - 1
        return counts