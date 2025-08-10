class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtrack(s, 0, [], res)
        return res

    def backtrack(self, s, start, path, res):
        if len(path) == 4 and start == len(s):
            res.append('.'.join(path))
            return
        if len(path) == 4 or start == len(s):
            return
        for i in range(start, min(start+3, len(s))):
            if (i > start and s[start] == '0') or int(s[start:i+1]) > 255:
                break
            path.append(s[start:i+1])
            self.backtrack(s, i+1, path, res)
            path.pop()