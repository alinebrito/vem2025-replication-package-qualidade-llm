class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        
        while num or k or carry:
            digit_sum = carry
            if num:
                digit_sum += num.pop()
            if k:
                digit_sum += k % 10
                k //= 10
            result.append(digit_sum % 10)
            carry = digit_sum // 10
        
        return result[::-1]