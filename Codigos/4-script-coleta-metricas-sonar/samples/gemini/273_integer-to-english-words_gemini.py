class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousands = 'Thousand Million Billion'.split()
        
        def words(n):
            if n < 20:
                return to19[:n]
            if n < 100:
                return [tens[n // 10 - 2]] + words(n % 10)
            if n < 1000:
                return [to19[n // 100 - 1], 'Hundred'] + words(n % 100)
            for i, v in enumerate(thousands):
                if n < 1000**(i + 2):
                    return words(n // 1000**i) + [v] + words(n % 1000**i)
        return ' '.join(words(num)) or 'Zero' 