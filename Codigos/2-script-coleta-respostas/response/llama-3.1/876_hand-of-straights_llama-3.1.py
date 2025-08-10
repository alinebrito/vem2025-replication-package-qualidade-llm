class Solution:
    def isNStraightHand(self, hand, groupSize):
        count = {}
        for num in hand:
            if num not in count:
                count[num] = 1
            else:
 count[num] += 1
        hand.sort()
        for num in hand:
            if count[num] > 0:
                for i in range(groupSize - 1, -1, -1):
                    if num + i not in count or count[num + i] < count[num]:
                        return False
                    count[num + i] -= count[num]
        return True