class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in sentence:
                return False
        return True