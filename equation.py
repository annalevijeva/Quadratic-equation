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
    if a != 0:
        if (b ** 2 - 4 * a * c) >= 0:
            x1 = ((-b) + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
            x1 = round(x1, 3)
            x2 = ((-b) - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
            x2 = round(x2, 3)
            solutions.append(x1)
            solutions.append(x2)
        else:
            pass
    else:
        if b != 0:
            x = - c / b
            x = round(x, 3)
            solutions.append(x)
        else:
            if c != 0:
                pass
    if len(solutions) == 0:
        return "This equation has no roots"
    else:
        return set(solutions)


def solve(args):
    if is_list_of_numbers(args):
        return equation(float(args[0]), float(args[1]), float(args[2]))
    else:
        return "Incorrect input.\na, b and c must be numbers. Using float numbers separate them with '.'"

# print(solve([0, -1, 9]))
