# Data Engineering YouTube Analysis Project

## Overview

This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

## Project Goals
1. 𝗗𝗮𝘁𝗮 𝗜𝗻𝗴𝗲𝘀𝘁𝗶𝗼𝗻: Built a robust mechanism using AWS S3 bucket for ingesting partitioned data from external source plus internal aws services.
2. 𝗘𝗧𝗟 𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝘀: Transformed raw CSV data to parquet after mapping correct schema changes and null validations. Certain region wise data was not encoded but filtered. So 
   data was filtered region wise using predicate pushdown. Parquet is a fast, optimized and efficient hybrid file storage format. Hence, proper format for meaningful 
   analysis.
   Used: AWS Glue, ETL jobs, Database, Tables and Crawlers to crawl data from S3 bucket.
3. 𝗗𝗮𝘁𝗮 𝗟𝗮𝗸𝗲: Established a centralized repository to efficiently store data from multiple sources and services. Stored raw, cleaned and transformed data using AWS S3 and 
   Glue Catalog.
4. 𝗗𝗮𝘁𝗮 𝗣𝗿𝗲-𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴: Semi-structured to Structured Data conversion. The raw json data was flattened and filtered on AWS Lambda function using python, pandas and aws 
   wrangler libraries to perform the read, write and stored the normalized json data in new cleaned S3 bucket in parquet format. A trigger was created to automate execution 
   of lambda function on data load in raw S3.
5. 𝗔𝗻𝗮𝗹𝘆𝘁𝗶𝗰𝘀: Constructed an insightful dashboard to analyze data and get key findings and answers. Used: AWS Athena for querying data and creating new analytics database. 
   AWS Quicksight - For dashboarding and BI service (offers cloud-based analytics).

## Steps Performed


1. Uploaded the data from my local machine into the S3 bucket using AWS CLI commands while trying to maintain a proper file organization. Stored the JSON and CSV files in       separate folders.
2. Used AWS Glue Catalog to crawl the data from JSON and CSV files from the raw bucket which would be stored in a separate database.
3. On facing issues raised due to the data in the JSON format, create a Python function using AWS Lambda to clean them and convert them into parquet format.
4. Created a trigger on this Lambda function so as to run every time new data is being added to S3 bucket and the output was stored in a new database in Athena.
5. Converted the CSV files into parquet format as well using AWS Glue ETL.
6. Created a new Glue Crawler to crawl the clean data into the database.
7. Now when all the clean data from the parquet files (converted from CSV and JSON files) is present in the same database, developed an ETL job using - AWS Glue Studio to 
   join both the tables and store it in a separate S3 bucket intended to use for BI purposes.
8. The data is now ready to be used for building dashboards out of it. I decided to analyze this data for finding out the popularity, most liked video categories, video 
   reach, engagement and likes to views comparison of channels in UK and Canada.


## Services we will be using
1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
2. AWS IAM: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
3. QuickSight: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
5. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.
6. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.
7) Python & Spark: To perform the ETL job in AWS Lambda and clean the data, Use the data in AWS Athena for Queries.


## Dataset Used
This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.

https://www.kaggle.com/datasets/datasnaek/youtube-new

## Conclusion:
1. The project demonstrates the potential impact and implications of leveraging cloud services for data transformation and analysis.
2. While real-time streaming is necessary for certain use cases, batch ingestion is often more effective and cost-efficient for analyzing large datasets and gaining 
   comprehensive insights.
3. Businesses can extract valuable insights, save costs, gain a competitive advantage, and ensure compliance with regulatory requirements by using cloud services.
4. The use of cloud services enables businesses to scale their data infrastructure and take advantage of powerful analytics tools without incurring the costs and 
   complexities of traditional data warehousing and ETL systems.

## Architecture Diagram
<img src="architecture.jpeg">
<![1695848460216](https://github.com/VidishaSharma26/Youtube-Data-analysis-End-to-end-Data-Engineering-project-/assets/132566486/d4e0d97e-0d35-4cfc-bdc3-994185076d9a)>



