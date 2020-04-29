class Person:
    def __init__(self,name,age,surname):
        self.name=name
        self.age=age
        self.surname=surname
    def display_info(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My surname is:",self.surname)
person1=Person("Ansar",17,"Amrin")
person1.display_info()


