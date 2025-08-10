class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0"*(len(b)-len(a)) + a
        else:
            b = "0"*(len(a)-len(b)) + b
        
        carry = 0
        result = ""
        
        for i in range(len(a)-1, -1, -1):
            sum_bits = int(a[i]) + int(b[i]) + carry
            result = str(sum_bits % 2) + result
            carry = sum_bits // 2
        
        if carry:
            result = "1" + result
        
        return result