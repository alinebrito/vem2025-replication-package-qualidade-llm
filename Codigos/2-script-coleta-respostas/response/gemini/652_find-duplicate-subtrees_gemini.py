class Solution:
    def findDuplicateSubtrees(self, root):
        def serialization(node, path):
            if node is None: return '#'

            path[serialization(node.left, path)] += 1
            path[serialization(node.right, path)] += 1
            return str(node.val) + ',' + str(path)
        
        ans = []
        count = collections.Counter()
        def dfs(node):
            if node is None:
                return
            
            path = collections.Counter()
            s = serialization(node, path)
            if count[s] == 1:
                ans.append(node)
            count[s] += 1

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans 