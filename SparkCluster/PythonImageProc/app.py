from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
import locale
locale.getdefaultlocale()
locale.getpreferredencoding()

# Limit cores to 1, and tell each executor to use one core = only one executor is used by Spark
conf = SparkConf().set('spark.executor.cores', 1).set(
    'spark.cores.max', 1).set('spark.executor.memory', '1g')
# sc = SparkContext(master='spark://spark-master:7077',
#                 appName='myAppName', conf=conf)

spark = SparkSession.builder.master(
    'spark://spark-master:7077').appName('Deforest').getOrCreate()
spark.conf.set('spark.executor.cores', 1)
spark.conf.set('spark.cores.max', 1)
spark.conf.set('spark.executor.memory', '1g')


print("done")
