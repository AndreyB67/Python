def kvadrat(x, y):
    return 1 / x ** abs(y)


print(kvadrat(2, -2))


def kvadrat_var2(x, y):
    for i in range(abs(y+1)):
        x *= x
    return 1 / x

print(kvadrat_var2(2, -2))