# Association
In Object-Oriented Programming (OOP), Association refers to the relationship between two or more objects where one object uses or interacts with another. It describes how objects are connected to each other and can communicate or work together.

(this part was by chatGPT, but I approve it.)

## Direction
The association between objects can be of one of two kinds:
- **Unidirectional** - Only one object is aware of the other object. (Ex: A person has a heart, but a heart doesn't have a person.)
- **Bidirectional** - Both objects are aware of eachother. (Ex: An owner has a bike, and a bike has an owner.)

Depending on the type of association, there might not be ownewship at all. Next part will cover that.


## Types of Association

- **One-to-One** - As the name implies. (Ex:A car has one engine.)
- **One-to-Many** - As the name implies. (Ex: A teacher has many students.)
- **Many-to-Many** - As name implies. (Ex: Many students enrolled in many courses. Pro tip, AVOID THESE!)
- **Aggregation** - When two objects are placed together, you can very easily separate them out and have them still work. If the whole is deleted, the part still exists. (Ex: If you destroy a station, the routes to it aren't destroyed.)
- **Composition** - When two objects are placed together, and if you separate them everything breaks. If one of them gets deleted, the other also stops existing. (Ex: If you pull the engine out of a car, the car ain't carring anymore.)

# Exercise - Library Management System
This is *your* exam. Yippee! Open books, good luck :3.
You will design a library management system. Do it step by step and you got this. You won't need to make a mini-project, you just need to demonstrate functionality.

1. Create the library class. The class is going to have a list/dictionary of books with varying quantities. Make sure the book is also a class of its own with appropiate variables (ISBN,name,author.).
2. Create a person class. The person can have a name, age, ID, stuff like that. Make sure the variables are private/public as they should be. Make an employee class which can restore the amount of books, and a customer class which can borrow books, inheriting the person class. Make sure to track the books that each person borrows, make sure they can't borrow more than x amount of books.
3. Test all the functions in a main, make sure it's all nice and cozy.



Good job, happyyyyyyyyyy holidays now that you're done! Hellish two weeks huh?