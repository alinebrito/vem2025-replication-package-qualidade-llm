class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}
        for card in deck:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
        x = -1
        for value in count.values():
            if value < 2:
                return False
            if x == -1:
                x = value
            elif x != value:
                gcd = self.gcd(x, value)
                if gcd < 2:
                    return False
                x = gcd
        return True

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a