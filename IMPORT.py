class computer :
    def __init__(self):
        self.age = 11
        self.name = "Ranuga"
    def Update(self):
        self.age = 545
c1 = computer()
print(c1.age)
c1.Update()
print(c1.age)
