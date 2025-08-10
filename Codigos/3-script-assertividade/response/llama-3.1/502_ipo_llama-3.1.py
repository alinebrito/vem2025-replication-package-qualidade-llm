class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        available_projects = []
        i = 0
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                available_projects.append(projects[i][1])
                i += 1
            if not available_projects:
                break
            w += max(available_projects)
            available_projects = []
            k -= 1
        return w