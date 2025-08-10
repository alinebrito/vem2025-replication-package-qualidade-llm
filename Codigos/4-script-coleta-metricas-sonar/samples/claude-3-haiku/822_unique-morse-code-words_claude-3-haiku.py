class Solution:
    def solution(self, words):
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformations = set()
        for word in words:
            transformation = ""
            for char in word:
                transformation += codes[ord(char) - ord('a')]
            transformations.add(transformation)
        return len(transformations)