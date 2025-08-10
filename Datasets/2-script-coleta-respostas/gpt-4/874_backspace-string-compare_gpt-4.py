class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_string(st):
            skip = 0  
            result = []
            for char in reversed(st):
                if char == '#':
                    skip += 1  
                elif skip:
                    skip -= 1  
                else:
                    result.append(char)
            return ''.join(reversed(result))
        
        return final_string(s) == final_string(t)