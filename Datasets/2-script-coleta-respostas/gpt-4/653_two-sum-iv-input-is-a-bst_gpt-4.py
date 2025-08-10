class Solution:
    def findTarget(self, root, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        nums = inorder(root)
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        return False