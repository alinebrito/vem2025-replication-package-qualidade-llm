class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for s in arr:
            mask = 0
            for c in s:
                idx = ord(c) - ord('a')
                if (mask >> idx) & 1:
                    mask = 0
                    break
                mask |= 1 << idx
            if mask:
                masks.append(mask)
        
        ans = 0
        def dfs(pos, mask):
            nonlocal ans
            ans = max(ans, bin(mask).count('1'))
 for i in range(pos, len(masks)):
                if mask & masks[i] == 0:
                    dfs(i + 1, mask | masks[i])
        
        dfs(0,0)
 return ans