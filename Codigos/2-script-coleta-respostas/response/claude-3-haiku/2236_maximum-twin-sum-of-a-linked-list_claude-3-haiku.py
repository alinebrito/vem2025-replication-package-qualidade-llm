class Solution:
    def pairSum(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        max_sum = 0
        for i in range(len(values) // 2):
            max_sum = max(max_sum, values[i] + values[len(values) - 1 - i])
        return max_sum