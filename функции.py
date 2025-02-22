№13 (1)
import numpy as np
import matplotlib.pyplot as plt
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
x_min = float(input("Введите минимальное значение x: "))
x_max = float(input("Введите максимальное значение x: "))
x = np.linspace(x_min, x_max, 100)
f_x = a + b * x**(3/2) + c * x**3
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, label='f(x) = a + b·x^(3/2) + c·x^3', color='blue')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

№13 (2) Координаты точек есть в файле "data"

import numpy as np
import matplotlib.pyplot as plt

x_values = []
y_values = []

with open("data.txt", "r") as file:
    for line in file:
        x, y = map(float, line.strip().split(','))
        x_values.append(x)
        y_values.append(y)
x_values = np.array(x_values)
y_values = np.array(y_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')
plt.title('График дискретных значений')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.show()
