
~/Desktop/hadoop-3.3.2/bin/hdfs dfs -rm /ols/Input/*
~/Desktop/hadoop-3.3.2/bin/hdfs dfs -rm -r /ols/Output

~/Desktop/hadoop-3.3.2/bin/hdfs dfs -put -f input.csv /ols/Input

~/Desktop/hadoop-3.3.2/bin/hadoop jar /home/kareem/Desktop/hadoop-3.3.2/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar \
-archives hdfs://localhost:9000/conda.tar \
-file ./mapper.py -mapper "conda.tar/miniconda3/bin/python mapper.py" \
-file ./reducer.py -reducer "conda.tar/miniconda3/bin/python reducer.py" \
-input /ols/Input -output /ols/Output

#~/Desktop/hadoop-3.3.2/bin/hdfs dfs -cat /ols/Output/*
rm -r ./output/*
~/Desktop/hadoop-3.3.2/bin/hdfs dfs -get /ols/Output/* ./output