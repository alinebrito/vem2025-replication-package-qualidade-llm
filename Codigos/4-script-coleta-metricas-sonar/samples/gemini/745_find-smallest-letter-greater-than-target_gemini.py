class Solution:
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
        return letters[0]