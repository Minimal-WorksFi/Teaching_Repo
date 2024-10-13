# Overview

This focuses on lists and their methods. It should be easy for you hopefully.

## What is the purpose of lists?
Lists (or arrays), are a good way to store variables together, as you did in the calculator app. Python lists are also really cool, because they have alot of methods already done. These methods are great because it makes it really easy to program.
Do you want to remove the first element from a list? Python's got you covered.

`array.pop(0)`

Do you want to clear a python list?

`array.clear()`

Do you want to sort a list?

`array.sort()`

## Learning resources

[List methods](https://pynative.com/python-list-exercise-with-solutions/)

## Exercises

Exercises with lists. You got this. Post them on your homework github repo.

### 1.0 Easy exercises

#### 1.1

Reverse a list and print it, easy enough.

Input:

`list1 = [100, 200, 300, 400, 500]`

Expected output:

`[500, 400, 300, 200, 100]`

#### 1.2

Square the list numbers and print them.

Input:

`numbers = [1, 2, 3, 4, 5, 6, 7]`

Expected output:

`[1, 4, 9, 16, 25, 36, 49]`

#### 1.3
Concatenate two lists together.

Input:

```python

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

```

Expected output:

`['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']`

#### 1.4
Iterate two lists simultaneously and print.

Input:

```python

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

```

Expected output:

```python

10 400
20 300
30 200
40 100

```


### 2.0 Challenging exercises :3.

Ooo, this is harder. Spooky. Try to solve these on your own.

### 2.1
Find the biggest sum between two numbers in a list.

Input:

```python

lst = [10, -10, 5, 2, 8, -2]

```

Expected output:

`18`

(Extra) Can you find the biggest power between two numbers in a list? :3.

### 2.2
Position changer, try to make a function that moves the indexes of each item in a list by k steps.
Input:

```python

lst = [1, 2, 3, 4, 5]
k = 2

```
Expected output:

`[4, 5, 1, 2, 3]`

### 2.3
List flattener, take all of the lists inside a list and merge them into one

Input:

```python

lst = [1, [2, [3, 4], [5]], 6]

```

Expected output:

`[1,2,3,4,5,6]`
