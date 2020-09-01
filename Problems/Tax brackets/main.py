def getTaxPercent(income):
    taxpercent = 0
    if income >=0 and income <= 15527:
        taxpercent = 0
    elif income >= 15528 and income <= 42707:
        taxpercent = 15
    elif income >= 42708 and income <= 132406:
        taxpercent = 25
    elif income >= 132407:
        taxpercent = 28

    return taxpercent

income = int(input())
percent = getTaxPercent(income)
calculated_tax = income * percent/100

print(f"The tax for {income} is {percent}%. That is {round(calculated_tax)} dollars!")