import matplotlib.pyplot as plt
import numpy as np
import os


def save_png(a, b, c):
    try:
        os.remove("static/images/g.png")
    except FileNotFoundError:
        pass
    a, b, c = float(a), float(b), float(c)
    x = np.linspace(-10, 10, 1000)
    y = a * (x ** 2) + b * x + c
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('Graph')
    plt.grid(True)
    plt.savefig("static/images/g.png")
    return
