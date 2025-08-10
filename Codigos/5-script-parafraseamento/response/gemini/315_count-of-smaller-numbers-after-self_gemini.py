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
            ret = []
            i = j = cnt = 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    ret.append(left[i])
                    cnt += j
                    self.count[left[i][0]] += cnt
                    i += 1
                else:
                    ret.append(right[j])
                    j += 1
            ret.extend(left[i:])
            ret.extend(right[j:])
            return ret

        enum = list(enumerate(nums))
        self.count = [0] * len(nums)
        sort(enum)