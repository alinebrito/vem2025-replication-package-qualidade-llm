class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        stack = []
        for char in S:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == K:
                    stack.pop()
            else:
                stack.append([char, 1])
        return ''.join(char * count for char, count in stack)