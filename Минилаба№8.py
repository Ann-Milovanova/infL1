import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

def true_function(x):
    return x ** 2 + np.sin(x)

np.random.seed(42)
x = np.linspace(-5, 5, 100)
y = true_function(x) + np.random.uniform(-1, 1, size=100)
models = {
    "SVR": SVR(kernel='rbf', C=100),
    "Random Forest": RandomForestRegressor(n_estimators=100),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100)
}
plt.figure(figsize=(18, 6))

X = x.reshape(-1, 1)

for i, (name, model) in enumerate(models.items(), 1):

    model.fit(X, y)
    y_pred = model.predict(X)

    mse = mean_squared_error(y, y_pred)

    plt.subplot(1, 3, i)
    plt.scatter(x, y, c='blue', s=20, label='Исходные точки')
    plt.plot(x, true_function(x), 'g--', linewidth=2, label='Истинная функция')
    plt.plot(x, y_pred, 'r-', linewidth=2, label='Предсказание')
    plt.title(f"{name}\nMSE: {mse:.2f}")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()