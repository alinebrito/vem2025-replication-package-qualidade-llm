class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        place_counts = collections.defaultdict(int)
        for i in range(6):
            for word in wordlist:
                place_counts[i, word[i]] += 1
        
        best_word = max(wordlist, key=lambda w: sum(place_counts[i, w[i]] for i in range(6)))
        matches = master.guess(best_word)
        
        if matches == 6:
            return
        
        new_wordlist = [w for w in wordlist if sum(w[i] == best_word[i] for i in range(6)) == matches]
        self.findSecretWord(new_wordlist, master)