# Data Engineering YouTube Analysis Project

## Overview

This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

## Project Goals
𝗗𝗮𝘁𝗮 𝗜𝗻𝗴𝗲𝘀𝘁𝗶𝗼𝗻: Built a robust mechanism using AWS S3 bucket for ingesting partitioned data from external source plus internal aws services.
𝗘𝗧𝗟 𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝘀: Transformed raw CSV data to parquet after mapping correct schema changes and null validations. Certain region wise data was not encoded but filtered. So data was filtered region wise using predicate pushdown. Parquet is a fast, optimized and efficient hybrid file storage format. Hence, proper format for meaningful analysis.
Used: AWS Glue, ETL jobs, Database, Tables and Crawlers to crawl data from S3 bucket.
𝗗𝗮𝘁𝗮 𝗟𝗮𝗸𝗲: Established a centralized repository to efficiently store data from multiple sources and services. Stored raw, cleaned and transformed data using AWS S3 and Glue Catalog.
𝗗𝗮𝘁𝗮 𝗣𝗿𝗲-𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴: Semi-structured to Structured Data conversion. The raw json data was flattened and filtered on AWS Lambda function using python, pandas and aws wrangler libraries to perform the read, write and stored the normalized json data in new cleaned S3 bucket in parquet format. A trigger was created to automate execution of lambda function on data load in raw S3.
𝗔𝗻𝗮𝗹𝘆𝘁𝗶𝗰𝘀: Constructed an insightful dashboard to analyze data and get key findings and answers. Used: AWS Athena for querying data and creating new analytics database. AWS Quicksight - For dashboarding and BI service (offers cloud-based analytics).


## Services we will be using
1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
2. AWS IAM: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
3. QuickSight: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
5. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.
6. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.

## Dataset Used
This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.

https://www.kaggle.com/datasets/datasnaek/youtube-new

## Architecture Diagram
<img src="architecture.jpeg">


