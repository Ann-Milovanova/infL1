# Часть специалиста по данным

import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs

X, y = make_blobs(
    n_samples=300, n_features=3, centers=3, cluster_std=1.2, random_state=42
)

data = pd.DataFrame(np.column_stack((X, y)), columns=["x", "y", "z", "class"])
data.to_csv("3d_classes.csv", index=False)
print("Данные сохранены в '3d_classes.csv'")


# Часть разработчика
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

data = pd.read_csv("3d_classes.csv")
X = data[["x", "y", "z"]].values
y = data["class"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

knn = KNeighborsClassifier()
knn_params = {"n_neighbors": [3, 5, 7], "weights": ["uniform", "distance"]}
knn_grid = GridSearchCV(knn, knn_params, cv=5)
knn_grid.fit(X_train, y_train)

svm = SVC(kernel="linear")
svm_params = {"C": [0.1, 1, 10], "gamma": ["scale", "auto"]}
svm_grid = GridSearchCV(svm, svm_params, cv=5)
svm_grid.fit(X_train, y_train)

print(f"Лучшие параметры KNN: {knn_grid.best_params_}")
print(f"Лучшие параметры SVM: {svm_grid.best_params_}")

# Часть дизайнера

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(131, projection="3d")
ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap="viridis", s=30)
ax1.set_title("Исходные данные")

ax2 = fig.add_subplot(132, projection="3d")
ax2.scatter(
    X_test[:, 0],
    X_test[:, 1],
    X_test[:, 2],
    c=knn_grid.predict(X_test),
    cmap="viridis",
    s=30,
)
ax2.set_title("KNN классификация")

ax3 = fig.add_subplot(133, projection="3d")
ax3.scatter(
    X_test[:, 0],
    X_test[:, 1],
    X_test[:, 2],
    c=svm_grid.predict(X_test),
    cmap="viridis",
    s=30,
)

xlim = ax3.get_xlim()
ylim = ax3.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
XX, YY = np.meshgrid(xx, yy)

for i in range(len(svm_grid.best_estimator_.coef_)):

    w = svm_grid.best_estimator_.coef_[i]
    b = svm_grid.best_estimator_.intercept_[i]

    ZZ = (-w[0] * XX - w[1] * YY - b) / w[2]

    ax3.plot_surface(
        XX, YY, ZZ, alpha=0.3, color="gray", rstride=5, cstride=5, linewidth=0
    )

ax3.set_title("SVM с полными гиперплоскостями")
plt.tight_layout()
plt.show()
#Графики к работе будут в файле "графики к кр№2 (2 семестр)"
