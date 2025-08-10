class Solution:
    def average(self, salary):
        avg = 0
        salary.sort()
        salary = salary[1:-1]
        avg = sum(salary) / len(salary)
        return avg