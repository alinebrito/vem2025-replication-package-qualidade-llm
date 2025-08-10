class Solution:
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.pushLeftBranch(root)

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def next(self) -> int:
        node = self.stack.pop()
        self.pushLeftBranch(node.right)
        return node.val

    def pushLeftBranch(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left