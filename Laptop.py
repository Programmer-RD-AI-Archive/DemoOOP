print(" > Welcome to laptop data center < ")
name = input(" > Please enter your laptops name... \n > ")
cpu = input(" > Enter the cpu type please... \n > ")
ram = int(input(" > Enter the Ram os your laptop please...  \n > "))
disapaly = int(input(" > Eneter display size of your laptop please.... \n > "))
class laptop :
    def __init__(self,name,cpu,ram,displaly):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.display = displaly
        