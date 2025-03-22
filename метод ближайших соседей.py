import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def generate_points(count, x_min, x_max, y_min, y_max, label):
    points = [[random.uniform(x_min, x_max), random.uniform(y_min, y_max)] for _ in range(count)]
    labels = [label] * count
    return points, labels

pointsCount1, pointsCount2 = 50, 50
xMin1, xMax1, yMin1, yMax1 = 2, 5, 2, 5
xMin2, xMax2, yMin2, yMax2 = 3, 10, 3, 10

x1, y1 = generate_points(pointsCount1, xMin1, xMax1, yMin1, yMax1, 0)
x2, y2 = generate_points(pointsCount2, xMin2, xMax2, yMin2, yMax2, 1)

x = x1 + x2
y = y1 + y2

def train_test_split(x, y, p=0.8):
    data = list(zip(x, y))
    random.shuffle(data)
    train_size = int(len(data) * p)
    train_data = data[:train_size]
    test_data = data[train_size:]
    x_train, y_train = zip(*train_data)
    x_test, y_test = zip(*test_data)

    return list(x_train), list(x_test), list(y_train), list(y_test)
x_train, x_test, y_train, y_test = train_test_split(x, y)

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def fit(x_train, y_train, x_test, k=3):
    y_predict = []
    for test_point in x_test:
        distances = [(euclidean_distance(test_point, train_point), label) for train_point, label in zip(x_train, y_train)]
        distances.sort(key=lambda x: x[0])
        k_nearest = [label for _, label in distances[:k]]
        most_common = Counter(k_nearest).most_common(1)[0][0]
        y_predict.append(most_common)
    return y_predict

y_predict = fit(x_train, y_train, x_test)

def computeAccuracy(y_test, y_predict):
    correct = sum(1 for yt, yp in zip(y_test, y_predict) if yt == yp)
    return correct / len(y_test)

accuracy = computeAccuracy(y_test, y_predict)
print(f'Accuracy: {accuracy:.2f}')

def visualize(x_train, y_train, x_test, y_test, y_predict):
    plt.figure(figsize=(8, 6))

    for i, point in enumerate(x_train):
        marker = 'o' if y_train[i] == 0 else 'x'
        plt.scatter(point[0], point[1], color='blue', marker=marker)

    for i, point in enumerate(x_test):
        if y_test[i] == y_predict[i]:
            color = 'green'
        else:
            color = 'red'
        marker = 'o' if y_test[i] == 0 else 'x'
        plt.scatter(point[0], point[1], color=color, marker=marker)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Метод k ближайших соседей')
    plt.show()
visualize(x_train, y_train, x_test, y_test, y_predict)
