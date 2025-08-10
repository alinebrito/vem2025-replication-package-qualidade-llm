class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def canDivide(s, t):
            return s == t * (len(s) // len(t))
        
        if str1 + str2 != str2 + str1:
            return ""
        
        length = gcd(len(str1), len(str2))
        candidate = str1[:length]
        
        if canDivide(str1, candidate) and canDivide(str2, candidate):
            return candidate
        
        return ""