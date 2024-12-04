# Overview
Refresher, inheritance and polymorphism. By now you've already worked with it a bit, but it's good to refresh on it a bit. Starting from now on, you will have to keep these ideas in mind, but I'm sure you'll find them natural.

## Inheritance
Inheritance is a fundamental part of OOP, as it allows new classes to be created from previously existant classes. This enables the reuse of code without having to write a lot more than previously. You will mainly use inheritance in a "is-a" type relationship.
Every car is a vehicle, so every car can do vehicle things. Yippee!
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print(f"{self.brand} is driving")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving fast")

# Usage
car = Car("Toyota", "Camry")
car.drive()  # Toyota Camry is driving fast
```

## Polymorphism
Polymorphism is about defining a consistent interface for different classes, allowing classes that have the same name for methods and functions to function differently. Think of it as more of a "every class can ___" relationship.
Every shape can be drawn.
```python
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Usage
shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()
# Output:
# Drawing a circle
# Drawing a square
```

(these parts were written in part with chatGPT, thank you ocean slurper)

# Exercise - Employee Management System
This time you will have one exercise, this is a *tiny* project that should ideally not take you too long.
1. You will create an Employee class with private attributes like `salary`, `performance`, and public variables like `name` and `rank`. Make appropiate methods that could be useful for an employee management system.
2. Create subclasses for the Employee class.
- **Manager Subclass**. This subclass can access other employees and approve leave, and/or change their salary/performance metrics. You can make the user login through this employee.
- **Developer**. This subclass does the same work as the regular employee, but they take a lot more time with it. You can make it so when the work function is called, there is a random chance that the developer writes code.
3. Create a main app for testing. You can log in directly through one of the managers of the company so don't worry about making a log in function. There will be a menu where you can choose to:
- Change salary/performance of chosen employee.
- Start work.
- Check employee file sheet
- Allow leave
- Quit

This project should be slightly bigger than the calculator, but significantly smaller than the game.