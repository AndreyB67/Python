def delenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Вы попытались разделить на 0"


print(delenie((int(input('Enter first number: '))), (int(input('Enter second number: ')))))
