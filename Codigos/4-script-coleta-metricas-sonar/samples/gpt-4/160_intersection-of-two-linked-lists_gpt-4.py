class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        
        currA, currB = headA, headB
        
        while currA is not currB:
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next
        
        return currA