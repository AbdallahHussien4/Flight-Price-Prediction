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

$HADOOP_HOME/bin/hdfs dfs -put -f ../data/preprocessed_test_data.csv /flight-price-prediction/Input

$HADOOP_HOME/bin/hadoop jar $HADOOP_STREAMING \
-file ./mapper_test.py -mapper "${CONDA_PYTHON} mapper_test.py" \
-file ./reducer_test.py -reducer "${CONDA_PYTHON} reducer_test.py" \
-file ./model.txt \
-input /flight-price-prediction/Input -output /flight-price-prediction/Output

rm ./score.txt
$HADOOP_HOME/bin/hdfs dfs -get /flight-price-prediction/Output/part* ./score.txt