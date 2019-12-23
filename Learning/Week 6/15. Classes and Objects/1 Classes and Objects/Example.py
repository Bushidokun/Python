class person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def display(self):
        print ("{} is {} years old and weighs {}kg".format(self.name, self.age, self.weight))

prins = person("Prins", 35, 85)
prins.display()