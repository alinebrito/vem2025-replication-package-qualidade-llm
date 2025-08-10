class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_count = [0] * 26
        for char in magazine:
            magazine_count[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if magazine_count[ord(char) - ord('a')] == 0:
                return False
            magazine_count[ord(char) - ord('a')] -= 1
        return True