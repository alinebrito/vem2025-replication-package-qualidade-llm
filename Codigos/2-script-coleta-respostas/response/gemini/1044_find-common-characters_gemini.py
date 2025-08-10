class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        for word in words:
            temp = []
            for c in word:
                if c in check:
                    temp.append(c)
                    check.remove(c)
            check = temp
        return check