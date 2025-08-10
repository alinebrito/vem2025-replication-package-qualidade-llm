class Solution(object):
    def judgeSquareSum(self, c):
        a = 0
        b = int(c**0.5)
        while a <= b:
            sum_of_squares = a**2 + b**2
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                a += 1
            else:
                b -= 1
        return False