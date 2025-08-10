class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        
        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                break
        else:
            return -1
        
        for j in range(length - 1, i, -1):
            if digits[j] > digits[i]:
                digits[i], digits[j] = digits[j], digits[i]
                break
        
        digits = digits[:i + 1] + sorted(digits[i + 1:])
        result = int(''.join(digits))
        
        return result if result <= 2**31 - 1 else -1