import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

datasets_list = []

noisy_circles = datasets.make_circles(n_samples=500, factor=0.5, noise=0.05, random_state=30)
datasets_list.append(('Two Circles', noisy_circles))

noisy_moons = datasets.make_moons(n_samples=500, noise=0.05, random_state=30)
datasets_list.append(('Two Moons', noisy_moons))

varied = datasets.make_blobs(n_samples=500, cluster_std=[1.0, 0.5], random_state=30, centers=2)
datasets_list.append(('Varied Blobs', varied))

x, y = datasets.make_blobs(n_samples=500, random_state=170, centers=2)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
x_aniso = np.dot(x, transformation)
aniso = (x_aniso, y)
datasets_list.append(('Anisotropic', aniso))

blobs = datasets.make_blobs(n_samples=500, random_state=30, centers=2)
datasets_list.append(('Blobs', blobs))

fig, axes = plt.subplots(5, 3, figsize=(18, 24))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

models = [
    ('KNN', KNeighborsClassifier(n_neighbors=3)),
    ('SVM', SVC(kernel='rbf', C=1.0, probability=True)),
    ('MLP', MLPClassifier(
        hidden_layer_sizes=(64, 32),
        activation='relu',
        solver='adam',
        max_iter=1000,
        random_state=42,
        early_stopping=True
    ))
]

for row_idx, (name, (x, y)) in enumerate(datasets_list):

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    for col_idx, (model_name, model) in enumerate(models):
        ax = axes[row_idx, col_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
        y_min, y_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                             np.linspace(y_min, y_max, 100))

        if hasattr(model, "predict_proba"):
            Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
        else:
            Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        markers = ['x', 'o']
        ax.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')

        for i in range(len(X_train)):
            ax.scatter(X_train[i, 0], X_train[i, 1],
                       marker=markers[y_train[i]],
                       c='blue', alpha=0.5, s=20)

        for i in range(len(X_test)):
            true_color = 'green' if y_test[i] == y_pred[i] else 'red'
            ax.scatter(X_test[i, 0], X_test[i, 1],
                       marker=markers[y_test[i]],
                       c=true_color, edgecolor='black', s=40)

        if row_idx == 0:
            ax.set_title(model_name)
        if col_idx == 0:
            ax.set_ylabel(name)

plt.savefig('classification_results.png', dpi=300)
plt.show()