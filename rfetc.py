
class car :
    Whells = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = car()
c2 = car()
c1.mil = 5
c1.Whells = 5
print(c1.com, c1.mil, c1.Whells)
print(c2.com, c2.mil,c2.Whells)
