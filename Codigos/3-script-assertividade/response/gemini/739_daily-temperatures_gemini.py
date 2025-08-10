class Solution:
    def dailyTemperatures(self, temps):
        n = len(temps)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temps[i] >= temps[stack[-1]]:
                stack.pop()
            if stack:
                answer[i] = stack[-1] - i
            stack.append(i)

        return answer