class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        dummy = TreeLinkNode(0)
        tail = dummy
        
        while root:
            if root.left:
                tail.next = root.left
                tail = tail.next
            if root.right:
                tail.next = root.right
                tail = tail.next
            root = root.next
            
            if not root:
                tail = dummy
                root = dummy.next
        
        return root