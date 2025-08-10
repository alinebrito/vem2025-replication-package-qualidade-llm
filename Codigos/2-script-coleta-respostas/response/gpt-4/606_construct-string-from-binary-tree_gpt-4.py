class Solution(object):
    def tree2str(self, t):
        if not t:
            return ""
        res = str(t.val)
        if t.left or t.right:
            res += "(" + self.tree2str(t.left) + ")"
        if t.right:
            res += "(" + self.tree2str(t.right) + ")"
        return res