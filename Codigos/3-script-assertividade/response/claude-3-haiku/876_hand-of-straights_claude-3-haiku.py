class Solution(object):
    def canSplit(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        for i in range(0, len(hand), groupSize):
            if hand[i] + groupSize - 1 != hand[i+groupSize-1]:
                return False
        return True