class Solution(object):
    def countCharacters(self, words, chars):
        count = 0
        for word in words:
            temp = chars
            flag = True
            for char in word:
                if char in temp:
                    temp = temp.replace(char, '', 1)
                else:
                    flag = False
                    break
            if flag:
                count += len(word)
        return count