class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return []
        greater_elements = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack:
                greater_elements[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        result = []
        for num in nums1:
            result.append(greater_elements.get(num, -1))
        return result