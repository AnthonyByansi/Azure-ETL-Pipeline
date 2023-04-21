import logging
import azure.functions as func
from pyspark.sql import SparkSession
from pyspark_job import transform_data

def main(req: func.HttpRequest, outputDocument: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Set up SparkSession
    spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

    # Read input data from Cosmos DB
    input_data = spark.read.format("cosmos.olap") \
        .option("spark.cosmos.container", "input-container") \
        .option("spark.cosmos.read.inferSchema.enabled", "true") \
        .load()

    # Transform the input data using PySpark
    output_data = transform_data(input_data)

    # Write the transformed data to Cosmos DB
    output_data.write.format("cosmos.oltp") \
        .option("spark.cosmos.container", "output-container") \
        .option("spark.cosmos.write.upsert.enabled", "true") \
        .option("spark.cosmos.write.upsert.col", "id") \
        .mode("append") \
        .save()

    return func.HttpResponse(f"Data successfully transformed and loaded to Cosmos DB.", status_code=200)
