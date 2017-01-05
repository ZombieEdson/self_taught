# parameter number in older editions of the book changed to n.
# Email cory@theselftaughtprogrammer.io for latest version


class AlwaysPositive:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return abs(self.number +
                   other.number)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)


print(x + y)
