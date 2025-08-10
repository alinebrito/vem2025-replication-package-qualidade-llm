class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s: str) -> str:
            result = []
            for char in s:
                if char == '#':
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return ''.join(result)
        
        return process_string(s) == process_string(t)