
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    def display(self):
        print("name:",self.name ) 
        print("Marks:",self.__marks)

    def getmarks(self) :
        return self.__marks
    
    def new_marks(self,newmark):
        if (newmark>=0):
            self.__marks=newmark

s1=Student("Ajay",85)
s1.display()