class Solution:
    def flatten(self, root):
        self.prev = None
        
        def flatten_tree(node):
            if not node:
                return
            flatten_tree(node.right)
            flatten_tree(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        
        flatten_tree(root)