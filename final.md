- 5 pts Abstract

- 20 pts Experiments/Analysis

  Detailed analysis of the analysis you ran and reasoning. Use visualizations when appropriate to explain any conclusions.
- 10 Comparisons:

  Specially for those groups that use popular kaggle datasets. If not, ensure you have several algorithms that you attempted to analyze the data with.
  
- 5 Conclusion

Code Running Instruction:
- In terminal, under the directory where the code are, run <em>python service.py</em>

  You'll see an initial screen containing: 
  
  - Welcome statement 
  - Service menu
  - User prompt for user to choose service
- Enter the number corresponding to the service you desired
- For service 1 [Wine Recommender]:
  - Follow the prompt to enter wine ID from 1 to 178
  
        - Invalid input will be captured and handled, and user will be asked to enter again
        - When input is valid, 5 random recommendations will be output
        - Then submenu with option [1: Try More] and [2: Back to Service Menu] will be provided for user to choose what to do next.
  - Follow the submenu to make next move
  
        - If user entered 1 [Try More], user can enter another wine ID to get recommendation, with the same prompt as above
        - If user entered 2 [Back to Service Menu], the initial screen will be shown again.
- For service 2 [Wine Region Analysis]:
- For service 3 [Wine Clustering]:
- or user can enter 4 to exit the program
