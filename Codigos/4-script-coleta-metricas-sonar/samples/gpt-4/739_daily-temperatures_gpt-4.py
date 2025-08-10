class Solution:
    def dailyTemperatures(self, temps):
        answer = [0] * len(temps)
        stack = []
        for i in range(len(temps)):
            while stack and temps[i] > temps[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx  
            stack.append(i)
        return answer  