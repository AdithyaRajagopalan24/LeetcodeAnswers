from sortedcontainers import SortedList

class MyCalendarThree:

    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> int:
        self.events.add((start, 1))
        self.events.add((end, -1))
        maxBook = currBook = 0
        for _, delta in self.events:
            currBook += delta
            maxBook = max(maxBook, currBook)
        return maxBook
