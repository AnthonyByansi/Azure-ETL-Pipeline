# Azure-ETL-Pipeline

This repository contains the code for a serverless ETL data pipeline built on Azure Functions. The pipeline reads data from a source database, performs transformations using Apache Spark, and writes the transformed data to a target database.

## Getting Started

To get started with the project, follow these steps:
1. Clone the repository
2. Set up your Azure account and create an Azure Functions app
3. Create the necessary input and output bindings in your Azure Functions app for your data source and target destination
4. Deploy the Azure Functions app to Azure
5. Run the pipeline by triggering the Azure Function

## Project Structure

The repository contains the following files and directories:
* `src/`: This directory contains the source code for the Azure Function that performs the ETL pipeline.
* `requirements.txt` : This file contains the necessary Python dependencies for the Azure Function.
* `pyspark_job.py`: This file contains the Apache Spark job code that performs the transformations.
* `README.md`: This file, which contains information about the project and how to use it
