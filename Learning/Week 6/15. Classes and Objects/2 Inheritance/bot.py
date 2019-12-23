class bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def get_age(self):
        print ("What is the age of bot?")
        self.age = int(input)

    def get_energy(self):
        print ("What is the bot energy level?")
        self.energy = int(input())

    def get_name(self):
        print ("What is the name of the bot?")
        self.name = input()

    def get_shield(self):
        print ("What is the bot shield level?")
        self.shield = int(input())
    
    def decrement_energy(self):
        self.energy -= 1
    
    def decrement_shield(self):
        self.shield -= 1

    def display_age(self):
        print (self.age)

    def display_energy(self):
        print (self.energy)

    def display_name(self):
        print (self.name)

    def display_shield(self):
        print (self.shield)

    def increment_age(self):
        self.age += 1

    def increment_energy(self):
        self.energy += 1
    
    def increment_shield(self):
        self.shield += 1
    
    def set_name(self):
        print ("What is the new name of the bot?")
        self.name = input()

prins = bot("Prins", 5, 15, 45)