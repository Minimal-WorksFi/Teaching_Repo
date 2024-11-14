from calculations import addition,subtraction,multiplication,division
from history import history

def val_input():
    a = float(input("input first number."))
    b = float(input("input second number."))
    return a,b

def main():
    run = True
    while run:
            op = int(input("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. History\n 6. Quit\n"))
            if op == 1:
                a,b = val_input()
                if addition(a,b):
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 2:
                a,b = val_input()
                if subtraction(a,b):
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 3:
                a,b = val_input()
                if multiplication(a,b):
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 4:
                a,b = val_input()
                if division(a,b):
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 5:
                history()
            else:
                run = False

if __name__ == "__main__":
    main()