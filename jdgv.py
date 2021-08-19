class student :

    school = "Vidura college"

    def __init__(self,n1,n2,n3):
        self.m1 = n1
        self.m2 = n2
        self.m3 = n3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)


    def getm1(self):
        return self.m1
    @classmethod
    def nfo(cls):
        return  cls.school
    @staticmethod
    def info():
        print("this is student class")

s1 = student(56565,54656,5656)
s2 = student(484,58,96)

print(s2.avg())

print(student.nfo())

student.info()