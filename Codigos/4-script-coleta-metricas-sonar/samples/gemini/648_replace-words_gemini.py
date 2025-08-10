class Solution:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = TrieNode()
        for root in dictionary:
            node = trie
            for char in root:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

        words = sentence.split()
        for i, word in enumerate(words):
            node = trie
            for j, char in enumerate(word):
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_word:
                    words[i] = word[:j+1]
                    break
        return ' '.join(words)