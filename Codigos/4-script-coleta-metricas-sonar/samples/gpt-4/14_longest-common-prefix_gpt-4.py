class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        if not v:
            return ""
        prefix = v[0]
        for s in v[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix  