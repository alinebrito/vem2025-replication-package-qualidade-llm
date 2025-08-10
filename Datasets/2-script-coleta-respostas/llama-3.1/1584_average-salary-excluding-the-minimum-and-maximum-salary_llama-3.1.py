class Solution:
    def average(self, salary):
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary) / len(salary)