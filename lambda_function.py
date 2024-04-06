#library used to access a nd read files present in S3
import awswrangler as wr
#data manipulation and analysis library for Python
import pandas as pd
#provides functions for parsing URLs and manipulating URL components.
import urllib.parse
#os provides a portable way of interacting with the operating system, including file system operations, environment variables, and process management.
import os

#retrieving environment variables related to AWS settings using the os.environ dictionary in Python
os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:

        # Creating DF from content reading the file
        df_raw = wr.s3.read_json('s3://{}/{}'.format(bucket, key))

        # Extract required columns that is item in our case:
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Write to S3 in parquet format
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )

        return wr_response
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
