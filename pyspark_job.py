from pyspark.sql.functions import col, to_date, year, month, dayofmonth

def transform_data(input_data):
    # Add a new column 'date' with the date parsed from the 'date_string' column
    input_data = input_data.withColumn("date", to_date(col("date_string"), "yyyy-MM-dd"))

    # Add new columns 'year', 'month', and 'day' from the 'date' column
    input_data = input_data.withColumn("year", year(col("date"))) \
        .withColumn("month", month(col("date"))) \
        .withColumn("day", dayofmonth(col("date")))

    # Select only the columns we need for the output
    output_data = input_data.select("id", "year", "month", "day", "value")

    return output_data
