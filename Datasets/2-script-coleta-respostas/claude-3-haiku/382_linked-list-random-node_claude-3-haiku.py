class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        if not self.head:
            return None

        current = self.head
        count = 1
        result = current.val

        while current.next:
            current = current.next
            count += 1
            if random.randint(1, count) == 1:
                result = current.val

        return result