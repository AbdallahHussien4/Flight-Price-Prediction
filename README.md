# Flight-Price-Prediction
This is a Machine Learning and Big Data Project to analyse the flight booking dataset obtained from the “Ease My Trip” website to predict the flight prices based on some features. 

## Dataset
[Flight Price Prediction](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)

## Prerequisites
- Linux
- Hadoop
- Anaconda/Miniconda
- Python
- Numpy
- Jupyter Notebook

## How to run
- To explore the dataset open the notebook 
`code/Data Analysis.ipynb`
- Modify the first 3 lines in `code/train.sh` and `code/test.sh` so it points to correct path, for example:
  ```
  export HADOOP_HOME=~/Desktop/hadoop-3.3.2
  export HADOOP_STREAMING=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar
  export CONDA_PYTHON=/home/kareem/miniconda3/bin/python
- Make sure hadoop is running
- To train the linear regression model on hadoop, run:  
  `cd code && ./train.sh`  
  the trained model is saved in `code/model.txt`
- To test the learned model on hadoop, run:  
  `cd code && ./test.sh`  
  the score is saved in `code/score.txt`

## Results
You Can see the results and details in the pdf documentations found above.

