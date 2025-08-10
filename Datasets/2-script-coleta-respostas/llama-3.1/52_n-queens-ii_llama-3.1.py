class Solution:
    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1]*n, 0, n)
        return self.res

    def dfs(self, nums, index, n):
        if index == n:
            self.res += 1 return
        for i in range(n):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index +1, n)

    def valid(self, nums, index):
        for i in range(index):
            if nums[i] == nums[index] or \
                nums[i] - i == nums[index] - index or \
                nums[i] + i == nums[index] + index:
                return False
        return True