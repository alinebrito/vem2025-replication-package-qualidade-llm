class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousands = 'Thousand Million Billion'.split()

        def helper(n):
            if n < 20:
                return to19[n - 1:n] if n else []
            elif n < 100:
                return [tens[n // 10 - 2]] + helper(n % 10)
            elif n < 1000:
                return [to19[n // 100 - 1]] + ['Hundred'] + helper(n % 100)
            else:
                for i, word in enumerate(thousands):
                    if n < 1000 ** (i + 1):
                        return helper(n // (1000 ** i)) + [word] + helper(n % (1000 ** i))

        return ' '.join(helper(num))