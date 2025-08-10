class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_val = max(nums)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(max_val)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max_val)+1:])