class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum += node.val
            count[curr_sum - targetSum] += 1
            self.result += count[curr_sum]
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            count[curr_sum] -= 1
        
        count = defaultdict(int)
        count[0] = 1
        self.result = 0
        dfs(root, 0)
        return self.result