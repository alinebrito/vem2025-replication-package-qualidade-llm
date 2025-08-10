class Solution:
    def wordPattern(self, pattern, str):
        words = str.split()
        if len(pattern) != len(words):
            return False

        pattern_dict = {}
        word_dict = {}

        for p, w in zip(pattern, words):
            if p not in pattern_dict:
                if w in word_dict:
                    return False
                pattern_dict[p] = w
                word_dict[w] = p
            else:
                if pattern_dict[p] != w:
                    return False

        return True