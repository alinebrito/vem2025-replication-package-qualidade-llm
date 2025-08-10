class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check: str) -> bool:
            return check == check[::-1]

        result = []
        word_dict = {word: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]

                if prefix in word_dict and i != word_dict[prefix] and is_palindrome(suffix + prefix):
                    result.append([i, word_dict[prefix]])

                if suffix in word_dict and i != word_dict[suffix] and is_palindrome(prefix + suffix):
                    result.append([word_dict[suffix], i])

        return result