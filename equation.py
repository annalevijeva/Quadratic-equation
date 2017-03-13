import math


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_list_of_numbers(args):
    for value in args:
        if is_number(value):
            pass
        else:
            return False
    return True


def equation(a, b, c):
    solutions = []
    if a == 0 and b == 0 and c == 0:
        return "True"
    elif a == 0 and b == 0:
        return "False"
    elif a == 0:
        # b*x + c = 0
        x = c / b
        solutions.append(x)
        return solutions
    elif b == 0:
        # a * x**2 + c = 0
        x = math.sqrt(c/a)
        solutions.append(x)
        solutions.append(-x)
        return solutions
    else:
        D = b**2 - 4*a*c
        if D > 0:
            x1 = ((-b) + math.sqrt(D)) / 2*a
            x2 = ((-b) - math.sqrt(D)) / 2*a
            solutions.append(x1)
            solutions.append(x2)
            return solutions
        elif D == 0:
            x = ((-b) + math.sqrt(D)) / 2*a
            solutions.append(x)
            return solutions
        else:
            return solutions


def solve(args):
    if is_list_of_numbers(args):
        return equation(float(args[0]), float(args[1]), float(args[2]))
    else:
        return "Incorrect input.\na, b and c must be numbers. Using float numbers separate them with '.'"

print(solve([0,0,0]))