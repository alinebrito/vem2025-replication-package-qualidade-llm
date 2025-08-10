class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        met_dot = met_e = met_num = False
        
        for i, c in enumerate(s):
            if c in '+-':
                if i > 0 and s[i-1] not in 'eE+-':
                    return False
            elif c == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif c.lower() == 'e':
                if met_e or not met_num:
                    return False
                met_e = True
                met_num = False
            elif c.isdigit():
                met_num = True
            else:
                return False
        
        return met_num