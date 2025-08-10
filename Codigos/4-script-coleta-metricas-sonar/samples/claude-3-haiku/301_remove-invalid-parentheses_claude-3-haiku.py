class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = {s}
        result = []
        visited = set()

        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        while level:
            valid_strings = []
            for curr in level:
                if is_valid(curr):
                    valid_strings.append(curr)
            if valid_strings:
                return valid_strings
            next_level = set()
            for curr in level:
                for i in range(len(curr)):
                    if curr[i] in '()':
                        next_level.add(curr[:i] + curr[i+1:])
                        visited.add(curr[:i] + curr[i+1:])
            level = next_level
        return result