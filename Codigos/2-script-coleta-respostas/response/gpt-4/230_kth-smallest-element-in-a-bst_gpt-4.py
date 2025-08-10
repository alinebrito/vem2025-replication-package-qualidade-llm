class Solution:
    def kthSmallest(self, root, k):
        self.k = k  
        self.result = None
        
        def inorder(node):
            if node is None:
                return  
            inorder(node.left)
            self.k -= 1  
            if self.k == 0:
                self.result = node.val  
                return  
            inorder(node.right)
        
        inorder(root)
        return self.result  