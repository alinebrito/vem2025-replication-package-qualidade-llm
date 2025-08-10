class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            chars = set(a)
            if len(chars) != len(a): continue
            for c in dp[:]:
                if chars & c: continue
                dp.append(chars | c)
        return max(len(s) for s in dp)