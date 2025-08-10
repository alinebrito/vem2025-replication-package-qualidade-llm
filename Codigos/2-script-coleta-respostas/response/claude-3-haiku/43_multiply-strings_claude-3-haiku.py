class Solution:
    def multiply(self, num1, num2):
        res = [0] * (len(num1)+len(num2))
        
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum = res[i+j+1] + mul
                res[i+j+1] = sum % 10
                res[i+j] += sum // 10
        
        while len(res) > 1 and res[0] == 0:
            res.pop(0)
        
        return ''.join(map(str, res))