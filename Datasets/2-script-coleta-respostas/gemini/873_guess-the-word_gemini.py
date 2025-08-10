class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        place_counts = collections.defaultdict(int)
        for word in wordlist:
            for i, char in enumerate(word):
                place_counts[(i, char)] += 1

        possible_words = wordlist
        guesses = 0
        while guesses < 10 and possible_words:
            best_word = None
            best_score = float('inf')

            for word in possible_words:
                score = sum(place_counts[(i, char)] for i, char in enumerate(word))
                if score < best_score:
                    best_score = score
                    best_word = word

            matches = master.guess(best_word)
            if matches == 6:
                return

            guesses += 1
            possible_words = [word for word in possible_words if sum(a == b for a, b in zip(word, best_word)) == matches]