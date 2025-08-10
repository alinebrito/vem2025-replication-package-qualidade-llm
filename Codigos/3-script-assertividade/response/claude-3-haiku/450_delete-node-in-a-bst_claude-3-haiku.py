class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self.findMinNode(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        
        return root
    
    def findMinNode(self, node):
        while node.left:
            node = node.left
        return node