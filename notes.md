# ML:

Field of study that gives computers the ability to learn without being programmed explicitly.

## Main types of ML:

1. Supervised learning
2. Unsupervised learning (Recommnder systems)
3. Reinforcement learning (Advanced recommenders)

## 1. Supervised learning: Train the algorithm using inputs and right outputs datasets --> 2 types:

+ Regression : First train the model with giving inputs mapped with correct outputs, then make it to predict accurate output for completely new input. Basically Model learns the relation between given datasets, then predicts the value according to that relation out of infinitely possible outputs. Ex :- House-price prediction
Here prediction is a number.

+ Classification: Same as regression but here, the predicted outputs will be among very few defined outputs unlike regression which predicts and returns output out of infinitely many possible outcomes. Ex :- Breast cancer detection (Malignant or Benign are the only two possible outputs).
Here prediction can be both numeric and non numeric (category).
Note: When classification takes more than 1 input, the model tries to draw a boundary that separates group of same kind of outputs and finally predicts output of new input based completely on which output's group/category it is lying in.

## 2. Unsupervised learning: Only predict something out of given input, no output label is predicted since we havent trained the model with possible output labels at all. The model majorly predicts something rather than being specific about any output (right answer for any given input). Itself determines patterns or groups.

+ Clustering - a type of Unsupervised learning used in Google news. Algorithm here reads hundreds of thousands of news on google and groups them into clusters based on similarity in the news (No specific predefined map as output while algorithm itself finds out pattern or cluster). No one is supervising it to output specific kind of output, meaning there's no one telling algorithm to find news articles giving it the topic or news name for every kind of news everyday, algorithm itself decides what to cluster.