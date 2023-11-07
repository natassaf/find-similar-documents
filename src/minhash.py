from pyspark import SparkContext
from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Docker Spark Example") \
    .master("spark://<YOUR_DOCKER_HOST_IP>:7077") \
    .getOrCreate()

# Create a Spark context
sc = spark.sparkContext

# Now, you can use sc and spark to run Spark jobs.
# For example:
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
