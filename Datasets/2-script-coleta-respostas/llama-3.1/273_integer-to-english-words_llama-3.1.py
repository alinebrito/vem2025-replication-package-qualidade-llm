class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        if num == 0:
            return 'Zero'
        res = ''
        if num >= 1000000000:
            res += self.numberToWords(num // 1000000000) + ' Billion '
            num %= 1000000000
        if num >= 1000000:
            res += self.numberToWords(num // 1000000) + ' Million '
            num %= 1000000
        if num >= 1000:
            res += self.numberToWords(num // 1000) + ' Thousand '
            num %= 1000
        if num >= 100:
            res += to19[num // 100] + ' Hundred '
            num %= 100
        if num >= 20:
            res += tens[num // 10 - 2] + ' '
            num %= 10
        if num > 0:
            res += to19[num - 1]
        return res.strip()