class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1
        return ''.join(merged)