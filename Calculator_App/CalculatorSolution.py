calculationHistory = []

def historyUpdate(a,b,operation,result):
    calculationHistory.append([a,b,operation,result])
    if len(calculationHistory) > 10:
        calculationHistory.pop(0)

def addition():
    a = float(input("input first number."))
    b = float(input("input second number."))
    print("Result is ", a + b)
    historyUpdate(a,b,"+",a + b)
    return True

def subtraction():
    a = float(input("input first number."))
    b = float(input("input second number."))
    print("Result is ", a - b)
    historyUpdate(a,b,"-", a - b)
    return True

def multiplication():
    a = float(input("input first number."))
    b = float(input("input second number."))
    print("Result is ", a * b)
    historyUpdate(a,b,"*", a * b)
    return True

def division():
    a = float(input("input first number."))
    b = float(input("input second number."))
    if (b == 0):
        return False
    print("Result is ", a / b)
    historyUpdate(a,b,"/", a / b)
    return True

def history():
    for calculation in calculationHistory:
        print(calculation[0],calculation[2],calculation[1], " = ", calculation[3])

def main():
    run = True
    while run:
            op = int(input("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. History\n 6. Quit\n"))
            if op == 1:
                if addition():
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 2:
                if subtraction():
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 3:
                if multiplication():
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 4:
                if division():
                    print("Operation succesful")
                else:
                    print("Failure")
            elif op == 5:
                history()
            else:
                run = False





if __name__ == "__main__":
    main()