class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha = {c: i for i, c in enumerate(order)}
        return all(s <= t for s, t in zip(words, words[1:])) or all(all(a == b for a, b in zip(s, t)) and len(s) < len(t) for s, t in zip(words, words[1:]))