class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        if not v:
            return ""

        prefix = v[0]
        for string in v[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix