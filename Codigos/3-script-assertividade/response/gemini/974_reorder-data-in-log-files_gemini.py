class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs,key = self.sort)
        
    def sort(self,log):
        id, rest = log.split(" ",1)
        if rest[0].isalpha():
            return (0, rest, id)
        else:
            return (1,)
