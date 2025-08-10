class Solution:
    def solution(self, words):
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformations = set()
        for word in words:
            transformation = ""
            for letter in word:
                transformation += codes[ord(letter) - ord('a')]
            transformations.add(transformation)
        return len(transformations)