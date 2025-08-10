class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxWealth = 0
        for customer in accounts:
            wealth = sum(customer)
            maxWealth = max(maxWealth, wealth)
        return maxWealth