class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        ptrA, ptrB = headA, headB

        while ptrA is not ptrB:
            ptrA = headB if ptrA is None else ptrA.next
            ptrB = headA if ptrB is None else ptrB.next

        return ptrA