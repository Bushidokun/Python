from bot import bot

class superbot(bot):
    def __init__(self, name, age, energy, shield, super_power_level = 10):
        super().__init__(name, age, energy, shield)
        self.super_power_level = int(super_power_level)

    def get_super_power_level(self):
        self.super_power_level += 1

    def set_super_power_level(self):
        print ("What is the super power level?")
        self.super_power_level = int(input())