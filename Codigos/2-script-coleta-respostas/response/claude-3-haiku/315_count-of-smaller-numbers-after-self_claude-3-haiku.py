class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            if len(enum) <= 1:
                return enum
            mid = len(enum) // 2
            left_part, right_part = sort(enum[:mid]), sort(enum[mid:])
            left_idx, right_idx = 0, 0
            result = []
            for i, num in enumerate(enum):
                if right_idx >= len(right_part) or (left_idx < len(left_part) and left_part[left_idx][1] > right_part[right_idx][1]):
                    result.append(len(right_part) - right_idx)
                    left_idx += 1
                else:
                    result.append(0)
                    right_idx += 1
            return list(zip(range(len(enum)), result))

        return [x[1] for x in sort(enumerate(nums))]