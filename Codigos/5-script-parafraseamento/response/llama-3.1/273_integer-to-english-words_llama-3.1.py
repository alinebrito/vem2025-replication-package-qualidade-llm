class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        below100 = {i: to19[i - 1] for i in range(1, 20)}
        below100.update({i: tens[i // 10 - 2] for i in range(20, 100, 10)})
        below100.update({i: tens[i // 10 - 2] + ' ' + to19[i % 10 - 1] for i in range(20, 100) if i % 10!= 0})
        thousands = ['', 'Thousand', 'Million', 'Billion']
        if num == 0:
            return 'Zero'
        res = ''
        i = 0
        while num > 0:
            if num % 1000!= 0:
                res = self.helper(num % 1000, below100) + ' ' + thousands[i] + ' ' + res
            num //= 1000
            i += 1
        return res.strip()
        
    def helper(self, num, below100):
        if num == 0:
            return ''
        elif num < 100:
            return below100[num]
        else:
            return below100[num // 100] + ' Hundred' + (' ' + below100[num % 100] if num % 100!= 0 else '')