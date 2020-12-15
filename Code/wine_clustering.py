import service
def wine_recommender():
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from tqdm import tqdm

    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.cluster import KMeans

    import pandas as pd

    pd.set_option('display.max_columns', None)
    pd.options.display.float_format = "{:.2f}".format

    # Reading and transforming the dataset into a pandas DataFrame from a csv file
    data_ori = pd.read_csv("Data/wine.csv")
    data_ori.rename( columns={'Unnamed: 0':'Wine ID'}, inplace=True )
    wine_IDs = data_ori['Wine ID']
    data = data_ori.copy()

    # dropping columns that won't be used for analysis: the first two columns(wine id/name, cultivar)
    data.drop(data.columns[[0,1]], axis = 1, inplace = True) 
    # print(data.head())
    # print("data_ori")
    # print(data_ori.head())

    # wine_IDs = np.arange(1, 179)
    # wine_IDs = data_ori.iloc[:, 0]
    # print(wine_IDs)

    # Prepare data for kmean algorithm by standardizing it
    std_scaler = StandardScaler()
    data_cluster=data.copy()
    data_cluster[data_cluster.columns]=std_scaler.fit_transform(data_cluster) 
    # Checking if the Standardization was made correctly, looking for mean=0 and std=1
    # print(data_cluster.describe()) 

    # Apply kmean algorithm with k = 3 
    kmeans = KMeans(n_clusters=3,random_state=17,init='k-means++')
    kmeans_labels = kmeans.fit_predict(data_cluster)

    centroids = kmeans.cluster_centers_
    pca_2 = PCA(2)
    pca_2_result = pca_2.fit_transform(data_cluster)
    centroids_pca = pca_2.transform(centroids)

    # pd.Series(kmeans_labels).value_counts()
    data['Cluster'] = kmeans_labels
    data['Wine ID'] = wine_IDs
    # print(data)
    unique_clusters = data["Cluster"].unique() 
    clusters = {}
    for cluster_i in unique_clusters:
        clusters.update({cluster_i : data[data['Cluster'] == cluster_i]})
    # print(clusters)

    # Make recommendation
    rec(data, wine_IDs, clusters)


# Make recommendation
def rec(data, wine_IDs, clusters):

    user_wine = input("\nPlease enter your favorite wine ID " + str((wine_IDs[0] + 1)) + " ~ " + str((wine_IDs.iloc[-1] + 1)) + ": ") 
    
    # Deal with invalid input
    input_invalid = True
    while input_invalid:

        if not user_wine.isnumeric() or int(user_wine) - 1 not in wine_IDs:
                print("Invalid input!")
                user_wine = input("\nPlease enter your favorite wine ID " + str((wine_IDs[0] + 1)) + " ~ " + str((wine_IDs.iloc[-1] + 1)) + ": ") 
        else:
            input_invalid = False
    # Examine to which cluster the wine user selected belong
    user_cluster = data[data['Wine ID'] == int(user_wine) -1]['Cluster']

    # Get all wines in the same cluster
    user_similar_wines = clusters[user_cluster.to_list()[0]]

    # Remove user selected wine from the cluster so it won't be recommended to the user again
    user_similar_wines = user_similar_wines[user_similar_wines['Wine ID'] != int(user_wine) -1]

    # Randomly pick 5 similar wines from the cluster to make recommendation to user
    user_might_like = user_similar_wines.sample(5)

    print("\nAccording to the chemical compostion, you might also like:\n")
    print(user_might_like['Wine ID'].to_list())

    # submenu for user to choose from, either try more or go back to service menu
    user_next = input('\nDo you want to 1: Try More   2: Back to Service Menu: ')

    # Handle invalid input
    input_invalid = True
    while input_invalid:
        if (user_next == '1'):
            input_invalid = False
            rec(data, wine_IDs, clusters)
        elif (user_next == '2'):
            input_invalid = False
            # service.service_func()
            service.service(service.service_func())
        else: 
            print("Invalid input!")
            user_next = input('\nDo you want to 1: Try more   2: Back to Menu: ')

if __name__ == '__main__':
    # wine_recommender.py executed as script
    wine_recommender()