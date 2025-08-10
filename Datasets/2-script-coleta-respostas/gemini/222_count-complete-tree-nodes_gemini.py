class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getLeftHeight(root)
        rightDepth = self.getRightHeight(root)
        if leftDepth == rightDepth:
            return 2**leftDepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def getLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def getRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height