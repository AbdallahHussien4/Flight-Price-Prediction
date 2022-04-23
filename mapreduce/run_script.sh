
hdfs dfs -rm /ols/Input/*
hdfs dfs -rm -r /ols/Output

hdfs dfs -put -f inputwords.txt /ols/Input

hadoop jar $HADOOP_STREAMING \
-file ./mapper.py -mapper "python3 mapper.py" \
-file ./reducer.py -reducer "python3 reducer.py" \
-input /ols/Input -output /ols/Output

hdfs dfs -cat /ols/Output/*