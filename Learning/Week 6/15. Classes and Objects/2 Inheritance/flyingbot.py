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



prins = flyingbot("Prins", 15, 20, 45, 70, 20)

print ("""Name = {}
Age = {}
Super power level = {}
Hover = {}""".format(prins.name, prins.age, prins.super_power_level, prins.hover))

prins.set_name()

print ("""Name = {}
Age = {}
Super power level = {}
Hover = {}""".format(prins.name, prins.age, prins.super_power_level, prins.hover))