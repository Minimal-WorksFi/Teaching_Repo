# Overview
This will be dense, and there's quite a bit of theory. You are going to learn how to concretely organize your projects and future work. What you learn here applies to all programming languages, you'll just have to use other design patterns and folder names and stuff.
We will be covering: 
- Scope (how it affects memory, and how variables are declared.)
- File organization patterns

Quite a lot of work, so we're going to jump into it.

# Scope
Scope is an important aspect of programming. If you understand it you will be able to understand file organization and how to go about it.

## What is scope?
Variables are limited to a "scope". Your eyes are probably rolling right now, "Great, what is scope then?". To do that, we will go a bit behind the scenes of the computer you have.

### Purpose of Scope
Your computer, has two *really* essential components, those are; the processor, and RAM (there are more components, but we will focus on these.). If you open your task manager, you can find those, and as you can notice and presumably know, they have a limited amount of resources available to themselves.

The processor does the calculations, the beep boops. You tell it ` 3 + 5 ` and it tells you `8`
The RAM **(Random Access Memory)**, takes the beep boops and keeps them for future use.
` a = 8 `

That's cool and all, but now you may be wondering, "isn't it possible for me to make toooooo many variables? Is there a way to make old variables just disapear into the aether?"

Why yes there is!

### Global and local scope
Scope is of two types: Global and local.

#### Global Scope
Global scope, pertains to variables and functions that can be accessed from anywhere from within the file you are in.
```python
food = "Banana"

def eat():
    print("I am eating the " + food)

def buy():
    print("I am buying the " + food)

buy()
eat()
```
The food variable, will be here forever in our RAM. But that is fine, cause I am currently thinking about bananas and bananas only. (I actually hate them honestly.)
But you can't just make 50000000000000 food strings for each and every single one of your needs, that would overwhelm your RAM.

With great power, comes even greater responsibility. Make as few global variables as possible, but don't shy away from using them when need be. It is important to note, the moment your program stops executing, the global variable gets ejected from RAM, so you can't fuck up your PC.

#### Local Scope
Local scope, pertains to variables and functions that can be accessed only from inside the function you're currently working in.
```python

def eat(food):
    print("I am eating the " + food)

def buy(food):
    print("I am buying the " + food)

buy("Groceries")
eat("Chocolate")
```
The food variable, exists inside the eat and buy function. The moment the function finishes or returns, the food variable gets ejected from the RAM, meaning you can't access it anymore and the computer can use that memory for something else.

### TLDR?
Scope represents the level of access and importance a variable has, if a variable is global, then it can be accessed from anywhere, but you also can't get rid of it. If a variable is local, then it can only be accessed from inside the function block you are currently in. Think of the project you're working on, what do you think would be the best global variables? What about local?


