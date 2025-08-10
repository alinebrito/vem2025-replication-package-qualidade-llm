class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []
        
        for word in words:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            
            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            
            if dp[-1]:
                result.append(word)
        
        return result