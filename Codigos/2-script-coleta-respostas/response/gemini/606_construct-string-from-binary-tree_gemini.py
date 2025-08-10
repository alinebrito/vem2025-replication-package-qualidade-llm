class Solution(object):
    def tree2str(self, t):
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        if t.left and not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"