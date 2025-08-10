class Solution:
    def uniqueMorseRepresentations(self, words):
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformations = set()
        for word in words:
            transformation = ''
            for char in word:
                transformation += codes[ord(char) - 97]
            transformations.add(transformation)
        return len(transformations)