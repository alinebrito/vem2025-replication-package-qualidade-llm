class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for person in people:
            result.insert(person[1], person)
        return result