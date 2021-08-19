class Computer :

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("the cpus and rams are", self.cpu, self.ram)
com1 = Computer('i7', 8)
com2 = Computer('i7', 4)
#Computer.config(com1)
#Computer.config(Computer())
com1.config()
com2.config()
