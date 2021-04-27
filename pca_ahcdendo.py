import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pandas import DataFrame
from sklearn import decomposition
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
from pandastable import Table
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
matplotlib.use('TkAgg')


def pcaplot(f, df):
    pcadf = df.copy()
    # set up factor analysis
    fa = decomposition.FactorAnalysis(n_components=2)
    #fit dataframe into factor analysis
    fa.fit(pcadf)
    scorelist = list()
    #store factor score in list
    for score in fa.score_samples(pcadf):
        scorelist.append(score)
    #convert list to dataframe
    df = DataFrame(scorelist, columns=['Factor Score'])
    rounded_df = df.round(6)
    #plot table with pandastable library
    pt = Table(f, dataframe=rounded_df)
    pt.show()


def dendoplot(df):
    # default setting of ahc
    cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', memory=None, connectivity=None,
                                      compute_full_tree='auto', linkage='ward', distance_threshold=None,
                                      compute_distances=True)
    pcadf = df.copy()
    result = cluster.fit(pcadf)

    def plot_dendrogram(model, **kwargs):
        # Create linkage matrix and then plot the dendrogram

        # create the counts of samples under each node
        counts = np.zeros(model.children_.shape[0])
        n_samples = len(model.labels_)
        for i, merge in enumerate(model.children_):
            current_count = 0
            for child_idx in merge:
                if child_idx < n_samples:
                    current_count += 1  # leaf node
                else:
                    current_count += counts[child_idx - n_samples]
            counts[i] = current_count

        linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)

        # Plot the corresponding dendrogram
        dendrogram(linkage_matrix, **kwargs)

    plt.title('Agglomerative Hierarchical Clustering Dendrogram')
    # plot the top three levels of the dendrogram
    plot_dendrogram(result, truncate_mode='level', p=3)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
