class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(start, parts):
            if parts == 4 and start == len(s):
                res.append('.'.join(segments))
                return
            if parts > 4 or start >= len(s):
                return

            for i in range(1, 4):
                segment = s[start:start+i]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                segments.append(segment)
                backtrack(start + i, parts + 1)
                segments.pop()

        segments = []
        backtrack(0, 0)
        return res