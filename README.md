| Name      | github username |
| ----------- | ----------- |
| Wei He      | RachelH2513 |
| Gabrielle   | gabrielleviray |
| Binwang Luo     | binwangluo  |

### Project Title: Using chemical analysis determine the origin of wines  


### Data Source
wine.data from
https://archive.ics.uci.edu/ml/machine-learning-databases/wine/

These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines.  


### Problem/Question
Italian wine is produced in every region of Italy, home to some of the oldest wine-producing regions in the world. People can choose hundreds of wine grape varieties from Italy. As is known to us, each kind of grape wine has different chemical composition, which decide the taste, smell and nutritional value.  
This project is based on the analyse the chemical of wine. The objective is to investigate the following in the same region in Italy:  
1. Cluster wines based on their chemical constituents.  
2. Content distribution of different constituents.  
3. Using chemical analysis determine the origin of wines.
4. With a someone's preference of a wine, we can show "what he/she may also interested in" with similar composition recommendation.


### Potential Methods
#### A. Preprossing.   
1. Identify all the attributes needed in the analysis.
2. Cleaning data and add column names.  
3. Do the basic basic statistics and visualization.  
  
#### B. Overlaying
Overlaying the attributes of the dataset to feed as input to the model.  

#### C. Operation  
We propose to do data analysis as input the following models to achieve the objective:  
1. Clustering
Different types of wine will be corresponding from different cultivars. This operation will help us to tell the chemical constituents when we know where a wine is from.  
2. Modeling.  
We'll mainly use Decision tree to decide on predicting possible outcomes which is a tree-like model. However this model may cost us much time on training.

### Outcome
#### A. Visualization
1. The chemistry interval distribution of all types of wine.   
2. The cluster of the wines contain similar chemistry.  
#### B. Purpose function 
When put in someone's preference of wine, we can get "what he/ she may also be interested in.  


——————————————————————————————————————————————————————————————————————————————————————
### Preliminary Analysis  

#### Dataset Analysis  
These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines. 
First cleaning the data.  
1. Slightly editing csv version (added column names) and check if there is missing value to fix.
2. confirming the count of attributes.  

Analysing the dataset we can see:  
1. There is the distribution's count of chemistry of wines. As we can see there are 13 types of chemical in wines recorded in this data set, which means we only analyse these 13 type of chemicals in this project. Proline is the highest content of some types of wine. And for most of wines, the content of Nonflavanoid phenols is the lowest.   
![image](https://github.com/RachelH2513/255-Team-1-Project/blob/main/images/Distribution1.jpg)  
2. From the diagram below, Alcohol is a most common chemistry for most wines. And some types of wines have special high or low content of some chemistry such as Magesium or makic acid(especially high in some wines) and Ash (especially low in some wines). These chemistry of wines can be used to determine the origin of wines.  
![image](https://github.com/RachelH2513/255-Team-1-Project/blob/main/images/Distribution2.jpeg)  
3. This is the results of a basic statistics. We can see the specific quantity of all types of wines. We can see that all wines have these 13 types of chemistry.   
![image](https://github.com/RachelH2513/255-Team-1-Project/blob/main/images/basic%20statistics.jpeg)  
4. The figure shows a scatter diagram by the 2 strongest principal components. We can see that there should be 3 clusters in corresponding to three types of wines from three different cultivars.
![image](https://github.com/RachelH2513/255-Team-1-Project/blob/main/images/Clusters.png)  

### Models for Operation
