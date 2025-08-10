class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort(log):
            identifier, *content = log.split()
            return (0, content) if content[0].isalpha() else (1,)
        return sorted(logs, key=sort)