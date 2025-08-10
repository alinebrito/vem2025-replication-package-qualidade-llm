class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA