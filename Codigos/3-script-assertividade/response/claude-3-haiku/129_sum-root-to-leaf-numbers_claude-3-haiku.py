class Solution:
    def sumNumbers(self, root):
        self.res = 0
        
        def dfs(node, curr_num):
            if not node:
                return
            
            curr_num = curr_num * 10 + node.val
            if not node.left and not node.right:
                self.res += curr_num
                return
            
            dfs(node.left, curr_num)
            dfs(node.right, curr_num)
        
        dfs(root, 0)
        return self.res