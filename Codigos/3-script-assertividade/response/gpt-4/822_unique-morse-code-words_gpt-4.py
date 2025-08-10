class Solution:
    def uniqueMorseRepresentations(self, words):
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                 ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformations = set()
        for word in words:
            transformation = "".join(codes[ord(letter) - ord('a')] for letter in word)
            transformations.add(transformation)
        return len(transformations)