class Solution:
    def is_palindrome(self, check):
            return check == check[::-1]
    def palindromePairs(self, words):
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if self.is_palindrome(words[i] + words[j]):
                        res.append([i, j])
        return res