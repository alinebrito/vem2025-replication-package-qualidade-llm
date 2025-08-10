class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        
        words = sentence.split()
        for i, word in enumerate(words):
            node = root
            for j, char in enumerate(word):
                if char in node.children:
                    node = node.children[char]
                    if node.is_end:
                        words[i] = word[:j+1]
                        break
                else:
                    break
        
        return ' '.join(words)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False