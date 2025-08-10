class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return  
            curr_sum += node.val  
            if curr_sum == targetSum:
                self.count += 1  
            self.prefix_sum[curr_sum] += 1  
            self.count += self.prefix_sum.get(curr_sum - targetSum, 0)
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            self.prefix_sum[curr_sum] -= 1

        self.count = 0  
        self.prefix_sum = defaultdict(int)
        dfs(root, 0)
        return self.count  