class Solution:
    def multiply(self, num1, num2):
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            carry = 0
            for j in range(len(num2)-1,-1,-1):
                temp = int(num1[i]) * int(num2[j]) + carry  
                carry = (res[i+j+1] + temp) // 10
                res[i+j+1] = (res[i+j+1] + temp) % 10
            res[i] += carry 
        res = ''.join(map(str,res))
        while res[0] == '0' and len(res)>1:
            res = res[1:]
        return res      