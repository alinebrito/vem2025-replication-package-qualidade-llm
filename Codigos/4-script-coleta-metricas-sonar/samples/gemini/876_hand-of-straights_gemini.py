class Solution(object):
    def find_successors(self, hand, groupSize, i, n):
        count = 0
        for j in range(n):
            if hand[j] == hand[i] + 1:
                count += 1
                i = j
        return count == groupSize - 1

    def isNStraightHand(self, hand, groupSize):
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        for i in range(n):
            if hand[i] != -1:
                val = hand[i]
                j = i
                count = 0
                while j < n and count < groupSize:
                    if hand[j] == val:
                        count += 1
                        hand[j] = -1
                        j += 1
                        val += 1
                    elif hand[j] > val:
                        break
                    else:
                        j += 1
                if count != groupSize:
                    return False
        return True