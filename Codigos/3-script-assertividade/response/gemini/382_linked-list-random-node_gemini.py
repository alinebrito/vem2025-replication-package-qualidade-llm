class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        count = 0
        curr = self.head
        chosen_value = curr.val
        while curr:
            count += 1
            if random.randint(1, count) == count:
                chosen_value = curr.val
            curr = curr.next
        return chosen_value