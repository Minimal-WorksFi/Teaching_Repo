# Overview
Object, oriented programming.
Whoaaaaaaaaa boy this is going to be a long one. Object oriented programming is a big paradigm in programming. It is useful, and, now that you finished the project, you will have a lot more oportunities opened up for yourself.

## Why Object Oriented programming?
Objects, what are they? Basically, objects are associations of data and functions, which allows for easy manipulation of data, and reusability of code. Cool right?

Let's pick an object to further demonstrate the point. A car.
You want to make a car drive for some time.
Think of how you'd program it now.
```python
car_name = "Subaru"
max_speed = 500 #kph
speed = 0
for i in range(0,10,1):
    if speed < max_speed:
        speed+=10
    print(car_name + " speed is: " + (str) speed + " kph")
```

Cool. This works. Make me another car now. Make me 5 cars now. Not so fun now? You probably hate yourself already just thinking about all the extra work. If only there were a way to just...type less.

Right, I think the points taken by now. An object "car" would fix the issue we're having here. Let's see,

## What is an object, and what is a class?
Classes are the blueprints from which you generate objects, and objects are instances of a class. Let's take the last example with the car.
The class of a car would then be:

```python
class Car():
    def __init__(self,car_name,top_speed):
        self.car_name = car_name
        self.top_speed = top_speed
        self.speed = 0
    
    def accelerate_change(self,change_of_speed):
        # We take both accelerations and decelerations here.
        self.speed += change_of_speed
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed
    
    def drive(self,drive_cycles):
        print("\n",self.car_name,"\n")
        for i in range(0,drive_cycles,1):
            self.accelerate_change(10)
            self.information()
        while(self.speed > 0):
            self.accelerate_change(-10)

    def information(self):
        print(self.car_name, " is driving at ", self.speed, " kph")
```

Okay, you're probably getting there; so this is how all the Car objects behave. What is a Car object then?

```python
car = Car("Subaru",200)
```

Okay, so the "Subaru" car object is an instance of the Car class.
```python
car.accelerate_change(10)
car.information()
```
Wowwwww, it works.
Let's apply it to the previous problem!

```python
class Car():
    def __init__(self,car_name,top_speed):
        self.car_name = car_name
        self.top_speed = top_speed
        self.speed = 0
    
    def accelerate_change(self,change_of_speed):
        # We take both accelerations and decelerations here.
        self.speed += change_of_speed
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed
    
    def drive(self,drive_cycles):
        print("\n",self.car_name,"\n")
        for i in range(0,drive_cycles,1):
            self.accelerate_change(10)
            self.information()
        while(self.speed > 0):
            self.accelerate_change(-10)

    def information(self):
        print(self.car_name, " is driving at ", self.speed, " kph")

if __name__ == "__main__":
    DRIVE_CYCLES = 15
    cars_list = [Car("Subaru",200),Car("Porsche",120),Car("Jeep",90)]
    for car in cars_list:
        car.drive(DRIVE_CYCLES)
        car.information()
```

Now we can drive multiple cars, all at the same time!
Awesome c:

You probably got a good hang of most of the class features by now, but below I will go into the definitions of each part of the class.

## Components of classes
1. Constructors
2. Variables
3. Methods

### 1. Constructor
The `def __init__(): ` method is the constructor. The constructor "constructs" instances of the class, thus, objects.

### 2. Variables
There are two types of variables in OOP. The instance variables, and the class variables.

- **Instance variables** are the ones you initialize using the `__init__` method. Instance variables are declared using the `self`.

- **Class variables** are the ones you initialize outside the `__init__`, or without using the `self`. These variables are useful if you want to record statistics. You will see an example of that in the demo.

#### What is the self?
Self tells you (and the computer), to access the object, and not the class itself. For example, in the car example, if you don't use the `self.top_speed`, then all cars would have the same top speed.

### 3. Methods
These are the functions associated with the class. They all call the `self` method to access the instance variables.


This concludes the lesson. Here is the [demo](./demo/car.py).

# Exercises