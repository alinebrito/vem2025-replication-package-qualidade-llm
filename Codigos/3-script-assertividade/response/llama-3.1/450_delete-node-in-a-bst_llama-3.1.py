class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            min_val = self.find_min(root.right)
            root.val = min_val
            root.right = self.deleteNode(root.right, min_val)
        return root

    def find_min(self, node):
        while node.left:
            node = node.left
        return node.val