class MyCalendarTwo:

    def __init__(self):
        self.bookings=defaultdict(int)
        

    def book(self, start: int, end: int) -> bool:
        self.bookings[start]+=1
        self.bookings[end]-=1
        count_book=0
        for book in sorted(self.bookings):
            count_book += self.bookings[book]
            if count_book >= 3:
                self.bookings[start]-=1
                self.bookings[end]+=1
                return False
        return True


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)