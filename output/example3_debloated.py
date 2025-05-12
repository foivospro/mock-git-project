from sklearn.cluster import KMeans
import math
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
kmeans = KMeans(n_clusters=2)