# Change this to your own path
export HADOOP_HOME=~/Desktop/hadoop-3.3.2
# Change this to your own path
export HADOOP_STREAMING=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar
# Change this to your own path
export CONDA_PYTHON=/home/kareem/miniconda3/bin/python

$HADOOP_HOME/bin/hdfs dfs -mkdir /flight-price-prediction
$HADOOP_HOME/bin/hdfs dfs -mkdir /flight-price-prediction/Input
$HADOOP_HOME/bin/hdfs dfs -rm /flight-price-prediction/Input/*
$HADOOP_HOME/bin/hdfs dfs -rm -r /flight-price-prediction/Output

$HADOOP_HOME/bin/hdfs dfs -put -f ../data/preprocessed_data.csv /flight-price-prediction/Input

$HADOOP_HOME/bin/hadoop jar $HADOOP_STREAMING \
-file ./mapper.py -mapper "${CONDA_PYTHON} mapper.py" \
-file ./reducer.py -reducer "${CONDA_PYTHON} reducer.py" \
-input /flight-price-prediction/Input -output /flight-price-prediction/Output

rm ./model.txt
$HADOOP_HOME/bin/hdfs dfs -get /flight-price-prediction/Output/part* ./model.txt