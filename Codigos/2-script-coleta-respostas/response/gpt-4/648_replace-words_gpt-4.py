class Solution:
    def replaceWords(self, dictionary, sentence):
        root_set = set(dictionary)
        words = sentence.split()
        
        def find_root(word):
            for root in sorted(root_set, key=len):
                if word.startswith(root):
                    return root
            return word
        
        return ' '.join(find_root(word) for word in words)