#inheretance
class Animal():
    def move(self):
        print("walk")

    def sound():
        pass


class Dog(Animal):
    def move(self):
        print("run")    #"polymorphism"
        
    def sound(self):
        print("barke")   #"polymorphism"  

class Snake(Animal):
     def move(self):
        print("crawl")   #"polymorphism"

     def sound(self):
        print("hiss")    #"polymorphism"


dog = Dog()
snake = Snake()

dog.move()
snake.move()
dog.sound()
snake.sound()

