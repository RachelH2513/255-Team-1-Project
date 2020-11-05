| Name      | github username |
| ----------- | ----------- |
| Wei He      | RachelH2513 |
| Gabrielle   | gabrielleviray |
| Roy Luo     | binwangluo  |

### Project Title: Who’ll win? Prediction of the Election’s result.

### Data Source
1. election-forecasts-2020.csv from
https://github.com/fivethirtyeight/data/tree/master/election-forecasts-2020

The data set contains records from 6/1/2020 to 10/9/2020. 
We can train the data to generate the model and then predict the furture records (after 10/9/2020) until 11/3/2020 the election day.

2. social medias API Twitter/Facebook
Facebook has its own voting channel that we assume we could take use of. 
Twitter provides APIs that search historical Tweets to analyze based on contextual, implicit topics or keywords. 
Refer to https://developer.twitter.com/en

### Problem/Question
Twitter has become an important communication channel of Election. People can announce a
viewpoint of election they’re observing with their smartphone. Based on these tweets, we can
statistic people’s preference of the election’s results.
This project will try multiple approaches to build different classifier model to predict the result of
election.

### Potential Methods
A brief description of the steps we will take to complete the project:
1. Data pre-processing: Importing libraries and data.
2. Data Analysis and Exploration
3. Data Cleaning: Only key words to be analyzed in each tweet.
4. Word cloud: Choose the word cloud for both electors’ supporters.
5. Vectorization of the pre-processed text
6. Build models and train.
7. Get the results.

### Measurement
The prediction is not only a result of who will win, but also it should include a ratio of the two
group’s supporters.
