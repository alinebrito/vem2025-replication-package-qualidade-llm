class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}
        for card in deck:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
        
        minCount = min(count.values())
        if minCount < 2:
            return False
        
        for x in range(2, minCount + 1):
            if all(c % x == 0 for c in count.values()):
                return True
        
        return False