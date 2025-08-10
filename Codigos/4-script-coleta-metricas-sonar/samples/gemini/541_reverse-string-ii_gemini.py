class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<(k):return s[::-1]
        ns=""
        for i in range(0,len(s),2*k):
            ns+=s[i:i+k][::-1]+s[i+k:i+2*k]
        return ns