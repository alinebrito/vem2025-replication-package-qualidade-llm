class Solution:
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False

        has_num = False
        has_e = False
        has_dot = False
        has_sign = False

        for i, char in enumerate(s):
            if char.isdigit():
                has_num = True
            elif char in ('+', '-'):
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
                has_sign = True
            elif char == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif char in ('e', 'E'):
                if has_e or not has_num:
                    return False
                has_e = True
                has_num = False  # Reset has_num after 'e' or 'E'
                has_dot = True  # Treat as if a dot is present after 'e' or 'E'
            else:
                return False

        return has_num