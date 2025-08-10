class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ptr = len(s) - 1
        t_ptr = len(t) - 1
        s_skip = 0
        t_skip = 0

        while s_ptr >= 0 or t_ptr >= 0:
            while s_ptr >= 0:
                if s[s_ptr] == '#':
                    s_skip += 1
                    s_ptr -= 1
                elif s_skip > 0:
                    s_skip -= 1
                    s_ptr -= 1
                else:
                    break

            while t_ptr >= 0:
                if t[t_ptr] == '#':
                    t_skip += 1
                    t_ptr -= 1
                elif t_skip > 0:
                    t_skip -= 1
                    t_ptr -= 1
                else:
                    break

            if s_ptr >= 0 and t_ptr >= 0 and s[s_ptr] != t[t_ptr]:
                return False

            if (s_ptr >= 0) != (t_ptr >= 0):
                return False

            s_ptr -= 1
            t_ptr -= 1

        return True