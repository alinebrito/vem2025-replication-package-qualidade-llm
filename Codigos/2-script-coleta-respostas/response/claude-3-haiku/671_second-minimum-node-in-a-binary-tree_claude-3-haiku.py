class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return -1
        
        left_min = root.left.val if root.left else float('inf')
        right_min = root.right.val if root.right else float('inf')
        
        if root.val < left_min and root.val < right_min:
            return max(left_min, right_min)
        
        left_second = self.findSecondMinimumValue(root.left)
        right_second = self.findSecondMinimumValue(root.right)
        
        if left_second != -1 and right_second != -1:
            return min(left_second, right_second)
        elif left_second != -1:
            return left_second
        else:
            return right_second