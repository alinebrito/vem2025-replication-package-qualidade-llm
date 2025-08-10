class Solution:
class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.calendar:
            if start < j and i < end:
                return False
        self.calendar.append((start, end))
        return True