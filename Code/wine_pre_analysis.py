import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.display.float_format = "{:.2f}".format

data = pd.read_csv("Data/wine.csv")
# print(data.head())
# dropping columns that won't be used for analysis
data.drop(data.columns[[0,1]], axis = 1, inplace = True) 
print(data.head())

# basic exploration of the data
print(data.info())
print ("No missing data in this data set.")

# Statistics
statistics = data.describe()
print(statistics)

# Plot histogram of each numerical variable
sns.set(style='white',font_scale=0.7, rc={'figure.figsize':(9,9)})
ax=data.hist(bins=20,color='red' )
# sns.displot(data['Proline'])
plt.show()

# boxplots
data.plot( kind = 'box', subplots = True, layout = (4,4), sharex = False, sharey = False,color='black')
plt.show()


# data_array = data.to_numpy()
# print (data_array)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(xs=data_array[0],ys=data_array[1],zs=data_array[2],zdir='z')
# plt.show()
# # plt.savefig("data_array.png", format="png")

std_scaler = StandardScaler()
data_cluster=data.copy()
data_cluster[data_cluster.columns]=std_scaler.fit_transform(data_cluster)


pca_2 = PCA(2)
pca_2_result = pca_2.fit_transform(data_cluster)

print ('Cumulative variance explained by 2 principal components: {:.2%}'.format(np.sum(pca_2.explained_variance_ratio_)))

sns.set(style='white', rc={'figure.figsize':(9,6)},font_scale=1.1)

plt.scatter(x=pca_2_result[:, 0], y=pca_2_result[:, 1], color='red',lw=0.1)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Data represented by the 2 strongest principal components',fontweight='bold')
plt.show()
