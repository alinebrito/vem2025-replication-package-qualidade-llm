class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, j = len(left), 0
                for i in range(len(enum))[::-1]:
                    if j == len(right) or m and left[m - 1][1] > right[j][1]:
                        smaller[left[m - 1][0]] += j
                        m -= 1
                        enum[i] = left[m]
                    else:
                        enum[i] = right[j]
                        j += 1
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller