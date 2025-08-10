class Solution:
    def getHint(self, secret, guess):
        bulls = sum(map(lambda x, y: x == y, secret, guess))
        cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - bulls  
        return f"{bulls}A{cows}B"