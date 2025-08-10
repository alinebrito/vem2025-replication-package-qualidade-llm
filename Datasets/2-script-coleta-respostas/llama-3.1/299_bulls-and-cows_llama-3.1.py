class Solution:
    def getHint(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        secret_count = {}
        guess_count = {}
        for s, g in zip(secret, guess):
            secret_count[s] = secret_count.get(s, 0) + 1
            guess_count[g] = guess_count.get(g, 0) + 1
        cows = 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls -= 1
            elif secret_count[s] > 0 and guess_count[g] > 0:
                cows += 1
                secret_count[s] -= 1
                guess_count[g] -= 1
        return f"{bulls}A{cows}B"