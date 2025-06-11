class Person:
    def __init__(self,name):
        self.name=name
    def display_info(self):
        print("Name:",self.name)
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks=marks
    def display_info(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
p1 = Person("Anil")
p1.display_info()
s2 = Student("Meera",92)
s2.display_info()