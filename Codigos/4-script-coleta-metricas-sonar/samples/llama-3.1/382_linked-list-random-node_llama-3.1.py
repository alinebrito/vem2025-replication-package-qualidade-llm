class Solution:
import random

class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            if random.random() < 1 / scope:
                chosen_value = curr.val
            curr = curr.next
            scope += 1
        return chosen_value