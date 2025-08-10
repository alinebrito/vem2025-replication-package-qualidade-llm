class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for char in s:
            if char.isalpha():
                res = [x + y for x in res for y in [char.lower(), char.upper()]]
            else:
                res = [x + char for x in res]
        return res