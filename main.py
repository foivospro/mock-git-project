#!/usr/bin/env python3

import numpy as np
from sklearn.cluster import KMeans

def main():
    # Use numpy and sklearn
    data = np.array([[1, 2], [3, 4], [5, 6]])
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(data)
    print(f"Cluster centers: {kmeans.cluster_centers_}")

if __name__ == "__main__":
    main()