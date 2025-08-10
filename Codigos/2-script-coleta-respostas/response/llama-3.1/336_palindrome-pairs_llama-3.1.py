class Solution:
    def palindromePairs(self, words):
        def is_palindrome(check):
            return check == check[::-1]

        word_index = {word: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left, right = word[:j], word[j:]
                if is_palindrome(right) and left[::-1] in word_index and word_index[left[::-1]] != i:
                    result.append([i, word_index[left[::-1]]])
                if j != len(word) and is_palindrome(left) and right[::-1] in word_index and word_index[right[::-1]] != i:
                    result.append([word_index[right[::-1]], i])
        
        return result