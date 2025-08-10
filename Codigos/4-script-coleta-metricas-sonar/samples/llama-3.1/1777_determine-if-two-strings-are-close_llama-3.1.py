class Solution:
 def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = {}
        count2 = {}
        for c in word1:
            if c in count1:
                count1[c] += 1
            else:
                count1[c] =1
        for c in word2:
            if c in count2:
                count2[c] += 1
            else:
                count2[c] = 1
        return sorted(count1.values()) == sorted(count2.values()) and set(word1) == set(word2)