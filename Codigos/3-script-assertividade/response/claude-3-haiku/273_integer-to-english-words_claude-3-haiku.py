class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'
        def helper(n):
            if n == 0:
                return ''
            elif n < 20:
                return to19.split()[n-1] + ' '
            elif n < 100:
                return tens.split()[n//10-2] + (' ' + helper(n%10) if n%10 else '')
            elif n < 1000:
                return helper(n//100) + 'Hundred' + (' ' + helper(n%100) if n%100 else '')
            elif n < 1000000:
                return helper(n//1000) + 'Thousand' + (' ' + helper(n%1000) if n%1000 else '')
            elif n < 1000000000:
                return helper(n//1000000) + 'Million' + (' ' + helper(n%1000000) if n%1000000 else '')
            else:
                return helper(n//1000000000) + 'Billion' + (' ' + helper(n%1000000000) if n%1000000000 else '')
        return 'Zero' if num == 0 else helper(num).strip()