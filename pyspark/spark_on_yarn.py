
import os
sys.path.append("/apache/spark3.1/python/lib/py4j-0.10.7-src.zip")
sys.path.append('/apache/spark3.1/python')
os.environ["SPARK_HOME"] = "/apache/spark3.1"
os.environ["PYSPARK_PYTHON"] = "./env/bin/python3"
import pyspark
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
import socket
notebook_ip = socket.gethostbyname(socket.gethostname())
print(notebook_ip)
notebook_port = "30203"
hadoop_queue = "***"
conf = SparkConf()
conf.setMaster("yarn").setAppName("Spark Example")
#conf.set("spark.deploy.mode","master")
conf.set("spark.driver.host", notebook_ip)
conf.set("spark.driver.port", notebook_port)
conf.set("spark.yarn.queue", hadoop_queue)
conf.set("spark.pyspark.python","./env/bin/python3")
conf.set("spark.archives", "hdfs://apollo-rno/user/b_aip/jialesun/env_py36.tar.gz#env")
sc = SparkContext(conf=conf)
print(sc.pythonExec)
print(sc.applicationId)
