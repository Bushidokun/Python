from Person import Person
class Employee(Person):
    def __init__(self, name, age, weight, employee_id):
        super().__init__(name, age, weight)
        self.employee_id = employee_id

    def display_employee_id(self):
        print(self.employee_id)