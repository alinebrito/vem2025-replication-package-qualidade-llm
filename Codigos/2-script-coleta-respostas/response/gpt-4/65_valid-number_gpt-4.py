class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        
        num_seen = False
        dot_seen = False
        e_seen = False
        sign_seen = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
            elif char in '+-':
                if sign_seen or (i > 0 and s[i-1] not in 'eE'):
                    return False
                sign_seen = True
            elif char == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char in 'eE':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                sign_seen = False
                num_seen = False
            else:
                return False
        
        return num_seen