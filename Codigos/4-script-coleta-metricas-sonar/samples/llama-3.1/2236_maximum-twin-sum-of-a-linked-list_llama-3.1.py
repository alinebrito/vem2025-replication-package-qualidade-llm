class Solution:
    def pairSum(self, head):
        nodes = []
        current = head
        while current:
            nodes.append(current.val)
            current = current.next
        max_sum = 0
        for i in range(len(nodes) // 2):
            max_sum = max(max_sum, nodes[i] + nodes[-i - 1])
        return max_sum