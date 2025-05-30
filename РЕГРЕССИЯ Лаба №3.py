import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

np.random.seed(42)
x_min, x_max = -2, 4
points = 50
x = np.linspace(x_min, x_max, points)

a_true, b_true, c_true = 2.0, 1.5, 3.0
y_true = a_true * (b_true ** x) + c_true
y = y_true + np.random.uniform(-3, 3, size=points)

def get_da(x, y, a, b, c):
    n = len(x)
    predictions = a * (b ** x) + c
    return (2 / n) * np.sum((predictions - y) * (b ** x))


def get_db(x, y, a, b, c):
    n = len(x)
    predictions = a * (b ** x) + c

    return (2 / n) * np.sum((predictions - y) * a * x * (b ** (x - 1)))


def get_dc(x, y, a, b, c):
    n = len(x)
    predictions = a * (b ** x) + c
    return (2 / n) * np.sum(predictions - y)

def fit(x, y, speed, epochs, a0, b0, c0):
    a, b, c = a0, b0, c0
    a_list = [a0]
    b_list = [b0]
    c_list = [c0]
    mse_list = []

    for i in range(epochs):
        da = get_da(x, y, a, b, c)
        db = get_db(x, y, a, b, c)
        dc = get_dc(x, y, a, b, c)

        a = a - speed * da
        b = b - speed * db
        c = c - speed * dc

        a_list.append(a)
        b_list.append(b)
        c_list.append(c)

        y_pred = a * (b ** x) + c
        mse = np.mean((y_pred - y) ** 2)
        mse_list.append(mse)

    return a_list, b_list, c_list, mse_list
    
speed = 0.001
epochs = 1000
a0 = 1.0
b0 = 1.1
c0 = 0.0

a_list, b_list, c_list, mse_list = fit(x, y, speed, epochs, a0, b0, c0)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
plt.subplots_adjust(bottom=0.25)


scatter = ax1.scatter(x, y, color='blue', label='Исходные данные')
x_plot = np.linspace(x_min, x_max, 100)
epoch_line, = ax1.plot(x_plot, a_list[0] * (b_list[0] ** x_plot) + c_list[0],
                       'r-', linewidth=2, label='Регрессия')
true_line, = ax1.plot(x_plot, a_true * (b_true ** x_plot) + c_true,
                      'g--', linewidth=1.5, label='Истинная функция')
ax1.set_title('Показательная регрессия: y = a·bˣ + c')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True)

mse_plot, = ax2.plot(mse_list, 'b-')
ax2.set_title('Среднеквадратичная ошибка (MSE)')
ax2.set_xlabel('Эпоха')
ax2.set_ylabel('MSE')
ax2.grid(True)
ax2.set_yscale('log')

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Эпоха', 0, epochs, valinit=0, valstep=1)



def update(val):
    epoch = int(slider.val)
    current_a = a_list[epoch]
    current_b = b_list[epoch]
    current_c = c_list[epoch]

    y_plot = current_a * (current_b ** x_plot) + current_c
    epoch_line.set_ydata(y_plot)

    ax1.set_title(f'Показательная регрессия (эпоха: {epoch}/{epochs})\n'
                  f'a = {current_a:.4f} (истинное: {a_true}), '
                  f'b = {current_b:.4f} (истинное: {b_true}), '
                  f'c = {current_c:.4f} (истинное: {c_true})')

    mse_plot.set_data(range(epoch), mse_list[:epoch])
    ax2.set_xlim(0, epochs)
    if epoch > 0:
        ax2.set_ylim(min(mse_list[:epoch]) * 0.9, max(mse_list[:epoch]) * 1.1)

    fig.canvas.draw_idle()


slider.on_changed(update)

update(0)

plt.tight_layout()
plt.show()
