class Solution:
    def summaryRanges(self, nums):
        ranges = []
        if not nums:
            return ranges
        start = nums[0]
        end = start
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))
                start = nums[i]
                end = start
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))
        return ranges