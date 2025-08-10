class Solution:
    def multiply(self, num1, num2):
        n1, n2 = len(num1), len(num2)
        pos = [0] * (n1 + n2)
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                sum = mul + pos[p2]

                pos[p1] += sum // 10
                pos[p2] = sum % 10

        res = ''
        for value in pos:
            if not (res == '' and value == 0):
                res += str(value)
        return '0' if res == '' else res