from superbot import superbot

class flyingbot(superbot):
    def __init__(self, name, age, energy, shield, super_power_level, hover = 0):
        super().__init__(name, age, energy, shield, super_power_level)
        self.hover = int(hover)

    def get_hover_distance(self):
        self.hover += 1

    def set_hover_distance(self):
        print("What is the hover distance?")
        self.hover = int(input())

print ("""Name = {}
Age = {}
Super power level = {}
Hover = {}""".function(self.name, self.age, self.super_power_level, self.hover))