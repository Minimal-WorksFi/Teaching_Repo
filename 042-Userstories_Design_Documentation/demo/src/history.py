calculation_history = []

def history_update(a,b,operation,result):
    calculation_history.append([a,b,operation,result])
    if len(calculation_history) > 10:
        calculationHistory.pop(0)

def history():

    for calculation in calculation_history:
        print(calculation[0],calculation[2],calculation[1], " = ", calculation[3])