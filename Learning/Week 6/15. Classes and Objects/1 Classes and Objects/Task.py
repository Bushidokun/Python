class Bot:
    def __init__(self, name, age, energy, shieldLevel):
        self.name = name
        self.age = str(age)
        self.energy = energy
        self.shieldLevel = str(shieldLevel)
    
    def display_name(self):
        print ("**" + ("*" * len(self.name)))
        print ("*" + self.name + "*")
        print ("**" + ("*" * len(self.name)))

    def display_age(self):
        print ("**" + ("*" * len(self.age)))
        print ("*" + self.age + "*")
        print ("**" + ("*" * len(self.age)))

    def display_energy(self):
        totalEnergy = 10
        print ("|", end="")
        print ("=" * self.energy, end="")
        print (" " * (totalEnergy - self.energy), end="")
        print ("|")
        print (self.energy)
    
    def display_shield(self):
        print ("**" + ("*" * len(self.shieldLevel)))
        print ("*" + self.shieldLevel + "*")
        print ("**" + ("*" * len(self.shieldLevel)))

    def display_summary(self):
        self.display_name()
        self.display_age()
        self.display_energy()
        self.display_shield()

    def __str__(self):
        return print ("""Name is {}
Age is {}
Energy is {}
Shield Level is {}""".format(self.name, self.age, self.energy, self.shieldLevel))

prins  = Bot("Prins", 10, 5, 50)
prins.display_age()
prins.__str__()