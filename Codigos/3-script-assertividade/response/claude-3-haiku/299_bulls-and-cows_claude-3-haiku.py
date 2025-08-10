class Solution:
    def getHint(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))
        cows = sum(min(secret.count(x), guess.count(x)) for x in set(secret)) - bulls
        return f"{bulls}A{cows}B"