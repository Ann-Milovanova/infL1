import numpy as np
import matplotlib.pyplot as plt

def func(x):
    """Трансцендентно-алгебраическая функция с минимумом"""
    return np.exp(-x ** 2) + x ** 2


def diff_func(x):
    """Аналитическая производная"""
    return -2 * x * np.exp(-x ** 2) + 2 * x

def gradient_descend(func=lambda x: x ** 2,
                     diff_func=lambda x: 2 * x,
                     x0=3.0,
                     speed=0.01,
                     epochs=100):
    """
    Параметры:
    func - оптимизируемая функция
    diff_func - производная функции
    x0 - начальная точка
    speed - скорость обучения
    epochs - количество итераций

    Возвращает:
    x_list, y_list - траектория движения к минимуму
    """
    x = x0
    x_list = []
    y_list = []

    for _ in range(epochs):
        x_list.append(x)
        y_list.append(func(x))
        x = x - speed * diff_func(x)

    return x_list, y_list


def plot_results(x_list, y_list):
    """Визуализация работы алгоритма"""
    x_vals = np.linspace(-2, 2, 400)
    y_vals = func(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Исходная функция')
    plt.scatter(x_list, y_list, c='red', s=40, label='Траектория спуска')
    plt.title('Градиентный спуск для f(x) = e^(-x²) + x²')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def find_critical_speed(x0=3.0, tolerance=1e-3, max_iter=100):
    """
    Бинарный поиск граничного значения скорости обучения
    Возвращает максимальную скорость, при которой метод сходится
    """
    low = 0.0
    high = 1.0
    threshold = 0.1

    for _ in range(max_iter):
        mid = (low + high) / 2
        x, _ = gradient_descend(func, diff_func, x0=x0, speed=mid, epochs=100)


        if abs(x[-1]) < threshold:
            low = mid
        else:
            high = mid

    return round((low + high) / 2, 4)

if __name__ == "__main__":

    x_points, y_points = gradient_descend(func, diff_func, x0=1.5, speed=0.1, epochs=50)
    print("Последняя точка:", x_points[-1])
    plot_results(x_points, y_points)

    critical_speed = find_critical_speed()
    print(f"Граничное значение скорости обучения: {critical_speed}")

    test_speeds = [critical_speed * 0.9, critical_speed * 1.1]
    for speed in test_speeds:
        x, _ = gradient_descend(func, diff_func, x0=1.5, speed=speed, epochs=50)
        status = "сходится" if abs(x[-1]) < 0.1 else "расходится"
        print(f"Скорость {speed:.4f}: {status}")