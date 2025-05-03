import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons, make_circles, make_classification
from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans
from sklearn.preprocessing import StandardScaler

def generate_data_1():
    return make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)


def generate_data_2():
    return make_moons(n_samples=300, noise=0.08, random_state=42)


def generate_data_3():
    return make_circles(n_samples=300, noise=0.05, factor=0.5, random_state=42)


def generate_data_4():
    X, _ = make_blobs(n_samples=300, random_state=170)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    return np.dot(X, transformation), _


def generate_data_5():
    return make_blobs(n_samples=300, cluster_std=[2.0, 0.5, 0.8], random_state=42)


def generate_data_6():
    X = np.random.rand(300, 2)
    return X, None

def dbscan_clustering(X):
    X = StandardScaler().fit_transform(X)
    db = DBSCAN(eps=0.3, min_samples=10).fit(X)
    return db.labels_


def agglomerative_clustering(X):
    agg = AgglomerativeClustering(n_clusters=3).fit(X)
    return agg.labels_


def kmeans_clustering(X):
    kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
    return kmeans.labels_

datasets = [
    (generate_data_1(), "Blobs"),
    (generate_data_2(), "Moons"),
    (generate_data_3(), "Circles"),
    (generate_data_4(), "Anisotropic"),
    (generate_data_5(), "Variance"),
    (generate_data_6(), "Random")
]

algorithms = [
    (dbscan_clustering, "DBSCAN"),
    (agglomerative_clustering, "Agglomerative"),
    (kmeans_clustering, "KMeans")
]

plt.figure(figsize=(15, 20))
plt.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.95, hspace=0.2, wspace=0.1)

for i, (dataset, title) in enumerate(datasets):
    X, y = dataset
    X = StandardScaler().fit_transform(X)

    for j, (algorithm, name) in enumerate(algorithms):
        plt.subplot(len(datasets), len(algorithms), i * len(algorithms) + j + 1)
        if i == 0:
            plt.title(name)

        try:
            labels = algorithm(X)
            plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=20)
        except Exception as e:
            print(f"Error in {name} for {title}: {e}")

        plt.xticks([])
        plt.yticks([])
        if j == 0:
            plt.ylabel(title)

plt.show()