class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [(root, 0, None)]
        x_info = None
        y_info = None

        while queue:
            node, depth, parent = queue.pop(0)

            if node.val == x:
                x_info = (depth, parent)
            elif node.val == y:
                y_info = (depth, parent)

            if x_info and y_info:
                break

            if node.left:
                queue.append((node.left, depth + 1, node))
            if node.right:
                queue.append((node.right, depth + 1, node))

        return x_info[0] == y_info[0] and x_info[1] != y_info[1]