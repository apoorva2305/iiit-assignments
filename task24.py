#create two base classes clock and calander based on this define a class calanderclock which inherits from both classes which displays month details date and time 
class Clock:
    def show_time(self):
        hour = input("Enter hour: ")
        minute = input("Enter minute: ")
        second = input("Enter second: ")
        print("Time:", hour + ":" + minute + ":" + second)


class Calendar:
    def show_date(self):
        day = input("Enter day: ")
        month = input("Enter month: ")
        year = input("Enter year: ")
        print("Date:", day + "/" + month + "/" + year)


class CalendarClock(Clock, Calendar):
    def display(self):
        self.show_date()
        self.show_time()


# Driver code
obj = CalendarClock()
obj.display()