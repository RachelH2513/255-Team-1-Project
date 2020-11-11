import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.display.float_format = "{:.2f}".format

data = pd.read_csv("Data/wine.csv")
# print(data.head())

print(data.info())
print ("No missing data in this data set.")
statistics = data.describe()
print(statistics)