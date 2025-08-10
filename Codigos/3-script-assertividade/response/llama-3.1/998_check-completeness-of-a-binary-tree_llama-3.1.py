class Solution:
    def isCompleteTree(self, root):
        queue = [root]
        flag = False
        while queue:
            node = queue.pop(0)
            if node.left:
                if flag:
                    return False
                queue.append(node.left)
            else:
                flag = True
            if node.right:
                if flag:
                    return False
                queue.append(node.right)
            else:
                flag = True
        return True