import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay

X, y = make_blobs(
    n_samples=300,
    n_features=3,
    centers=3,
    cluster_std=1.5,
    center_box=(-10, 10),
    random_state=42,
)

data = pd.DataFrame(
    np.hstack([X, y.reshape(-1, 1)]), columns=["x1", "x2", "x3", "class"]
)
data.to_csv("3d_classes.csv", index=False)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

knn = KNeighborsClassifier()
param_grid_knn = {"n_neighbors": [3, 5, 7, 9], "weights": ["uniform", "distance"]}
grid_knn = GridSearchCV(knn, param_grid_knn, cv=5)
grid_knn.fit(X_train, y_train)
print(f"Лучшие параметры KNN: {grid_knn.best_params_}")

svm = SVC(kernel="linear")
param_grid_svm = {"C": [0.1, 1, 10], "gamma": ["scale", "auto"]}
grid_svm = GridSearchCV(svm, param_grid_svm, cv=5)
grid_svm.fit(X_train, y_train)
print(f"Лучшие параметры SVM: {grid_svm.best_params_}")

fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(131, projection="3d")
ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap="viridis")
ax1.set_title("Исходные данные")

ax2 = fig.add_subplot(132, projection="3d")
ax2.scatter(
    X_test[:, 0], X_test[:, 1], X_test[:, 2], c=grid_knn.predict(X_test), cmap="viridis"
)
ax2.set_title("KNN классификация")

ax3 = fig.add_subplot(133, projection="3d")
ax3.scatter(
    X_test[:, 0], X_test[:, 1], X_test[:, 2], c=grid_svm.predict(X_test), cmap="viridis"
)

for i in range(len(grid_svm.best_estimator_.coef_)):
    w = grid_svm.best_estimator_.coef_[i]
    b = grid_svm.best_estimator_.intercept_[i]

    xx, yy = np.meshgrid(np.linspace(-15, 15, 10), np.linspace(-15, 15, 10))
    zz = (-w[0] * xx - w[1] * yy - b) / w[2]
    ax3.plot_surface(xx, yy, zz, alpha=0.3, color="gray")

ax3.set_title("SVM с разделяющими гиперплоскостями")

plt.tight_layout()
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

disp_knn = DecisionBoundaryDisplay.from_estimator(
    grid_knn.best_estimator_, X[:, [0, 1]], response_method="predict", alpha=0.5, ax=ax1
)
disp_knn.ax_.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k")
ax1.set_title("KNN (2D проекция)")

disp_svm = DecisionBoundaryDisplay.from_estimator(
    grid_svm.best_estimator_, X[:, [0, 1]], response_method="predict", alpha=0.5, ax=ax2
)
disp_svm.ax_.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k")
ax2.set_title("SVM (2D проекция)")

plt.show()
