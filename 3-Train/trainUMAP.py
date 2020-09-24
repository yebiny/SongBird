from sklearn.cluster import KMeans
import umap
import numpy as np
import matplotlib.pyplot as plt

def get_kmeans_labels(data, n_clusters):
    kmeans_labels = KMeans(init="k-means++", n_clusters=n_clusters, random_state=0, max_iter = 5).fit(data).labels_
    return kmeans_labels

def umap_embedding(data, n_neighbors=50, save=None):

    fit = umap.UMAP(
        n_neighbors=n_neighbors,
        min_dist=0.1,
        n_components=2,
        metric='euclidean'
        )
    umaped = fit.fit_transform(data);
    print(umaped.shape)

    if save!=None:
        np.save('%s/umaped'%save, umaped )

    return umaped

def plot_cluster(data, labels, save=None):
    x = data[:,0]
    y = data[:,1]

    fig=plt.figure(figsize=(8,6))
 
    c = plt.scatter(x, y, c=labels, cmap='gist_rainbow', marker='.')
    plt.colorbar(boundaries=np.arange(max(labels)+2)-0.5).set_ticks(np.arange(max(labels)+1))

    plt.scatter(x, y, c=labels, cmap='gist_rainbow', marker='.')
    if save!=None:
        plt.savefig(save)
    
    
    plt.show()
    
def plot_project(data_2d, c_lenth=1, save=None):

    x = data_2d[:,0]
    y = data_2d[:,1]


    if type(c_lenth)==int:
        fig=plt.figure(figsize=(6,6))
        c = plt.scatter(x, y, marker='.', c='black', alpha=0.4)      
    else:
        fig=plt.figure(figsize=(8,6))
        #colors = (c_lenth-np.min(c_lenth))/(np.max(c_lenth)-np.min(c_lenth))
        c = plt.scatter(x, y, c=c_lenth, cmap='jet', marker='.')
        plt.colorbar(c)
    if save!=None:
        plt.savefig(save)
    plt.show()
