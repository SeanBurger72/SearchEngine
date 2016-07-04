import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

  conf = SparkConf().setAppName("Spark Count")
  sc = SparkContext(conf=conf)

  threshold = int(sys.argv[2])

  tokenized = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))

  wordCounts = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1 +v2)

  list = wordCounts.collect()
#  print repr(list)[1:-1]
