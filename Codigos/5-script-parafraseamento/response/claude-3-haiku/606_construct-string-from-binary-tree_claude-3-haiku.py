class Solution:
    def tree2str(self, t):
        if not t:
            return ""
        
        left = "({})".format(self.tree2str(t.left)) if t.left else ""
        right = "({})".format(self.tree2str(t.right)) if t.right else ""
        