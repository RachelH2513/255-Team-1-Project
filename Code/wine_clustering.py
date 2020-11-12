import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm
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