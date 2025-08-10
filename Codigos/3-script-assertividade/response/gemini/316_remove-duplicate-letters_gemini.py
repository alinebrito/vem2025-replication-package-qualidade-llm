class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {}
        
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(s[i])
                stack.append(s[i])
        