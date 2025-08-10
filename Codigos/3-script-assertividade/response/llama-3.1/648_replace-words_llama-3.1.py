class Solution:
    def replaceWords(self, dictionary, sentence):
        words = sentence.split()
        root = {}
        for word in dictionary:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word
        res = []
        for word in words:
            node = root
            for char in word:
                if char not in node:
                    break
                node = node[char]
            if '#' in node:
                res.append(node['#'])
            else:
                res.append(word)
        return ' '.join(res)