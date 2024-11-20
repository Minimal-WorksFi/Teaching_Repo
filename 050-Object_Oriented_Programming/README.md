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
## 1. Passenger Transportation
I want to play OpenTTD. I hate sitting here and being stuck at uni. I want to have fun. Make me the fun game.

You will create a train class (choo choo). I will give you the main function, and you try to figure out how to make the Train class. choo choo.
```python
from random import randint
if __name__ == "__main__":
    passenger = 1000
    timer = 0
    while(passenger > 0):
        passenger_capacity = randint(50,300)
        passenger_currently = randint(20,100)
        train = Train(passenger_currently,passenger_capacity,timer)
        train.load_passengers(passenger)
        train.information()
        timer = timer + randint(5,10)
```
Output similar to:
```
Train 1 has 20 passengers. Loading 143 passengers.
Train 1 has departed with 163 passengers at 0 minutes. Max capacity is 163
Station currently has: 857 passengers

Train 2 has 75 passengers. Loading 38 passengers.
Train 2 has departed with 113 passengers at 8 minutes. Max capacity is 113
Station currently has: 819 passengers

Train 3 has 52 passengers. Loading 78 passengers.
Train 3 has departed with 130 passengers at 16 minutes. Max capacity is 130
Station currently has: 741 passengers

Train 4 has 83 passengers. Loading 37 passengers.
Train 4 has departed with 120 passengers at 24 minutes. Max capacity is 120
Station currently has: 704 passengers

Train 5 has 30 passengers. Loading 52 passengers.
Train 5 has departed with 82 passengers at 34 minutes. Max capacity is 82
Station currently has: 652 passengers

Train 6 has 28 passengers. Loading 96 passengers.
Train 6 has departed with 124 passengers at 41 minutes. Max capacity is 124
Station currently has: 556 passengers

Train 7 has 62 passengers. Loading 64 passengers.
Train 7 has departed with 126 passengers at 50 minutes. Max capacity is 126
Station currently has: 492 passengers

Train 8 has 52 passengers. Loading 7 passengers.
Train 8 has departed with 59 passengers at 57 minutes. Max capacity is 59
Station currently has: 485 passengers

Train 9 has 92 passengers. Loading 137 passengers.
Train 9 has departed with 229 passengers at 62 minutes. Max capacity is 229
Station currently has: 348 passengers

Train 10 has 42 passengers. Loading 34 passengers.
Train 10 has departed with 76 passengers at 72 minutes. Max capacity is 76
Station currently has: 314 passengers

Train 11 has 26 passengers. Loading 263 passengers.
Train 11 has departed with 289 passengers at 77 minutes. Max capacity is 289
Station currently has: 51 passengers

Train 12 has 71 passengers. Loading 51 passengers.
Train 12 has departed with 122 passengers at 84 minutes. Max capacity is 173
Station currently has: 0 passengers
```

## 2. Fuel Efficiency
You are going to create a new car class. The car class is going to have:
- Fuel efficiency
- Fuel
- Name

You will make a race between 10 cars or so, and you will then rank them by distance travelled. You have no main class now. Figure it out :3.
Possible output:
```
1. Car 9 (Travelled 750 kms)
2. Car 1 (Travelled 720 kms)
3. Car 10 (Travelled 720 kms)
4. Car 2 (Travelled 705 kms)
5. Car 6 (Travelled 648 kms)
6. Car 5 (Travelled 600 kms)
7. Car 7 (Travelled 598 kms)
8. Car 4 (Travelled 540 kms)
9. Car 3 (Travelled 516 kms)
10. Car 8 (Travelled 363 kms)
```