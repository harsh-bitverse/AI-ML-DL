# ML

Field of study that gives computers the ability to learn without being programmed explicitly.

## Main types of ML (Based on amount of supervision required)

1. Supervised learning
2. Unsupervised learning (Recommnder systems)
3. Reinforcement learning (Advanced recommenders)

### 1. Supervised learning: Data used to train model comes with Input X and Output Y labels. --> 2 types

+ Regression: Basically Model learns the relation between given datasets, then predicts the value according to that relation out of infinitely possible numerical outputs.
Ex :- House-price prediction.
Here prediction is a number.

+ Classification: Same as regression but here, the predicted outputs will be among very few defined outputs unlike regression which predicts and returns output out of infinitely many possible outcomes.
Ex :- Breast cancer detection (Malignant or Benign are the only two possible outputs).
Here prediction can be both numeric and non numeric (category).

Note: When classification takes more than 1 input, the model tries to draw a boundary that separates group of same kind of outputs and finally predicts output of new input based completely on which output's group/category it is lying in.

### 2. Unsupervised learning: Data used to train the models comes with Input X but not with Output Y labels. Algorithm finds a strcuture out of the data. --> 3 types

+ Clustering - grouping similar data points together(structure here is cluster).
Ex :- Google News: Algorithm here reads hundreds of thousands of news on google and groups them into clusters based on similarity in the news (No specific predefined map as output while algorithm itself finds out pattern or cluster). No one is supervising it to output specific kind of output, meaning there's no one telling algorithm to find news articles giving it the topic or news name for every kind of news everyday, algorithm itself decides what to cluster.

+ Anamoly detection - finds unusual data point.
Ex :- Fraud detection in Banking system.

+ Dimensionality reduction - compress data using fewer columns of input while losing as less information as possible. There will be instances where if many columns of  inputs are removed, even then it wouldn't have much affect on the output produced. Thus in such cases, we need to reduce the dimension of input to make the algorithm work more efficiently and faster.
Ex :- Mnsit data set.

+ Association rule based learning - Mined data are used as input to learn the pattern and associate the inputs together.
Ex :- In shopping malls or grocery stores, why are eggs kept near to the milk stall? It was seen that customers who bought milk also had bought eggs. Here data of bills produced are processed and output patterns are observed (mined) to gather associative patterns.

<!-- Data Mining : When the algorithm is derived after training the model over the data, if I derive required information like "On what logic, if this algorithm working?" then that is called Data Mining. Basically, deriving data from derived logic/ algorithm. -->

### 3. Semisupervised learning: Where few input output labellings are done manually, rest are done by machine

Ex :- Google photos - here when you click photos, google asks for the name of the person in the pic, once one person's photo is named, then rest of all the photos where such a person is seen in the photo, will be labelled automatically.

### 4. Reinforcement learning : Data is not fed manually. The machine learns the data too on itw own

Ex :- Self driving cars do not have pre-defined data, they run on roads, do mistakes, learn from them.

## Main types of ML (Based on how the ML is trained (Production - server on which code runs))

### 1. Batch/Offline learning: Where the model is trained over large chunk of data on local machine and the learnt model is then deployed in production environment --> USED WHERE THERE IS NO CONCEPT DRIFTING OR VERY LESS FREQUENT DRIFTING (Information about a well defined species of organism, Image classification etc)

This is where the model once trained and deployed onto production environment, after certain time period, the model again needs to be pulled back to local to train it with the old + new data and again deploy it which is a big disadvantage of it. Thus we use Online learning.

Ex :- Netflix (every week)

### 2. Online learning: Where the model is incrementally trained in mini batches in the server itself (Predict + Learn) --> USED WHERE THERE IS CONCEPT DRIFTING i.e, Constantly new data is emerging and the model needs to be upto date (Finance, Medical, etc)

Ex :- All chat bots, YouTube

## Main types of ML (Based on how the ML learns)

### 1. Instance-based learning (Memorizing): Where model doesn't learn anything from data until the instance when the new data is given to model to predict its output. Then model simply calculates the distance of the new data point from the nearest N data points and predicts output based on outputs of these N data points (lazy learners - storage heavy - needs complete data set everytime to decide output)

Ex :- KNN, Kernel

### 2. Model-based learning (Generalizing): Where model runs on data points and learns the relationship between input and output to draw the final decision curve to judge the output of the incoming new point who's output to be predicted. After acquiring the curve, if the data points are removed, still the incoming data point's output can be predicted (that is model has learnt the underlying principles of deciding the output) (not storage heavy since it needs to store only the equation rather than data set)

Ex :- Majority of models

## Problems in ML

+ Availability of Data: Data isn't easily available in real world.
+ Insufficient data: If data is huge, then irrespective of the model we use, we get same result, while if the data is small (which does, in real life), models do matter in that case.
+ None representative data: If data is not present fully, then the decision curve drawn by model might be halfway or not accurate since the full data can have significantly different decision curve.
+ Poor quality data: Data isn't present in proper format, few data are missing, non concluded data, etc.
+ Irrelevant features: Feeding grabage data gives a grabage output. Feeding relevant data based on the kind of output we need.
+ Overfitting: When model doesn't learn the underlying relationship between input and outputs, then it can give correct outputs only for the data on which it was trained rather than predicting correct outputs of new incoming data.
+ Underfitting: When model doesn't get trained well on the data, rather model tries to draw easiest curve possible which might not always give correct predictions.
+ Software Integration: Building end-to-end products will be difficult since a model need not be compatible everywhere.
+ Offline learning
+ Cost involved: Building products is not enough, get users to use it, handle the operations and costs to get real world experience of cost handling

## MLDLC - Machine Learning Development Life Cycle

1. Framing the problem: Stating problem correctly, roadmap, what algorithms, what's the budget, what's the expected output, etc
2. Gathering Data: Through APIs, Web scrapping, etc
3. Data pre-processing: Remove duplicates, remove missing values, remove outliers, scale down to standardised form, etc
4. Exploratory Data Analysis (EDA): Plot graphs, understand the variations in data, etc
5. Feature(input columns) Engineeing and Selection: Create new features either from existing features or newly
6. Model training (Modelling), Evaluation and Selection: Feeding the data to many kind of models, evaluate the accuracies based on metrics and finally select the model to use
7. Model Deployment: Deploy on servers for users to use
8. Testing: Allow trusted users to use it and take actions on their feedback, A/B Testing, etc
9. Optimize: Updating the data and retraining the model with modern new steps, along with maintaing the operations over large chunk of users

