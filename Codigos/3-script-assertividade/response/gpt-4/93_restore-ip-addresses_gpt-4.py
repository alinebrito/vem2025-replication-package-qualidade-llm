class Solution:
    def restoreIpAddresses(self, s):
        res = []
        def backtrack(start, path):
            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return
            for i in range(1, 4):
                if start + i <= len(s):
                    part = s[start:start + i]
                    if (part[0] != '0' or len(part) == 1) and 0 <= int(part) <= 255:
                        backtrack(start + i, path + [part])
        backtrack(0, [])
        return res