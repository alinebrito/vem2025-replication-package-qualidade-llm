class Solution(object):
    def countCharacters(self, words, chars):
        chars_count = {}
        for char in chars:
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1
        
        good_strings_length = 0
        for word in words:
            word_count = {}
            for char in word:
                if char in word_count:
                    word_count[char] += 1
                else:
                    word_count[char] = 1
            
            is_good = True
            for char, count in word_count.items():
                if char not in chars_count or count > chars_count[char]:
                    is_good = False
                    break
            
            if is_good:
                good_strings_length += len(word)
        
        return good_strings_length