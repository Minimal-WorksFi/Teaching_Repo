from history import history_update

def addition(a,b):
    print("Result is ", a + b)
    history_update(a,b,"+",a + b)
    return True

def subtraction(a,b):
    print("Result is ", a - b)
    history_update(a,b,"-", a - b)
    return True

def multiplication(a,b):
    print("Result is ", a * b)
    history_update(a,b,"*", a * b)
    return True

def division(a,b):
    if (b == 0):
        return False
    print("Result is ", a / b)
    history_update(a,b,"/", a / b)
    return True

if __name__ == "__main__":
    addition(1,5)
    subtraction(3.33,2.5)
    multiplication(3.33,3)
    division(5,2)
    division(0,0)
