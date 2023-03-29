from pyspark.sql import SparkSession
# from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType

from datetime import datetime
spark = SparkSession.builder.appName("GCS to BigQuery").getOrCreate()

start_date=datetime.today().strftime('%Y.%m.%d')



bucket_name = "nifibucket1"
folder_path = f"gs://{bucket_name}/{start_date}/"


df = spark.read.json(folder_path)
df.printSchema()

table_name = "analytics.pyspark"

df.write.format("bigquery") \
    .option("table", table_name) \
    .option("temporaryGcsBucket", bucket_name) \
    .mode("append") \
    .save()

# df.write.format("bigquery") \
#     .option("table", table_name) \
#     .option("temporaryGcsBucket", bucket_name) \
#     .option("credentialsFile", "/home/denemegcp/eloquent.json") \
#     .mode("append") \
#     .save()


