"""#classes
class Color ():
    def black(self):
        print("black")
    def red(self):
        print("red")


color = Color()
color.black()
color.red()
color.blue ="blue"
print(color.blue)

color2=Color()
color2.black()
color2.red()
"""""

"""#constructors
class Circle():
    def __init__(self,r):
        self.r = r

    def diameter(self):
        d = 2 * self.r
        print(f'diameter equals {d}')

circle =Circle(5)
circle.diameter()
print(circle.r)

circle2 = Circle(3)
circle2.diameter()
print(circle2.r)
"""

"""Abstraction 
class Animal():
    def move(self):
        pass
    def sound(self):
        pass
"""

#lab 
class Student() :
    def name(self):
        return" haidy" 
    def age(self):
        return"23"
student = Student()
student.name()
student.age() 
print(f'the student name is {student.name()} and his age is {student.age()}')

