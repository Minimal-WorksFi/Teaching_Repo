# Overview
You will have a refresher on encapsulation, and abstraction. These two go hand in hand well together, and the exercises will match that. Ever since this, you will have to use abstraction and encapsulation for your OOP work.

## Encapsulation
Encapsulation is a fundamental principle in OOP that involves bundling data (fields) and methods (functions) that operate on that data into a single unit called a class. The primary goal of encapsulation is to restrict direct access to some components of an object to ensure the integrity and security of the data.
Its benefits are:
- Data hiding
- Controlled Access
- Maintainability
- Security

## Abstraction
Abstraction is an OOP principle that focuses on hiding the implementation details of a system and showing only the essential features or functionalities to the user. It simplifies complex systems by breaking them into smaller, more manageable units and exposing only what is necessary.
Its benefits are:
- Simplification of complex stuff. (yuck)
- Modularity (the ability to turn code into tiny pieces)
- Easier refactoring (as long as you don't change the input or output,which is a *bad* idea anyways)
- Reusability

### How does Abstraction Work?

Abstraction works mainly by using abstract classes and interfaces. Interfaces aren't much of a thing in python, so you will only learn about abstract classes.

Abstract classes are classes which have functions that do nothing, those functions are the abstract methods. Their purpose is to make sure that whichever class inherits it, will have those functions explicited.
```python
from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
rect = Rectangle(5, 10)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
```

(these parts were written in part with chatGPT, thank you ocean slurper)


# Exercises

None of these exercises requrie a fully functional app, focus on demonstrating the way the code works rather than making fully functional apps, like in the projects so far. You got this.

## 1. Bank Class.

I want an ultra secure bank. The bank will hold multiple values, wether it be in a list or dictionary. Create setters,getters and the like for the bank. Make sure I can't break in and just steal money from the bank, and make some test functions.

## 2. Shapes

Take the shape example, create multiple kinds of shapes based on the example. Circles, triangles, squares, hexagons if you're freaky.

## 3. Vehicle Simulator

I want to play OpenTTD again. So time to make you suffer.
You will have to make multiple set of objects, all based on the abstract vehicle class. The classes *have* to fulfill different functionalities. I.E: A bus carries passengers, a train has stations.