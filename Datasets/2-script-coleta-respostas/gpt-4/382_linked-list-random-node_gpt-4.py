class Solution:
import random

class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        chosen_value = None
        curr = self.head
        count = 0
        while curr:
            if random.randint(0, count) == 0:
                chosen_value = curr.val
            count += 1
            curr = curr.next
        return chosen_value