# DataEnginner-Youtube_Statistics
![Banner Image](https://raw.githubusercontent.com/CD-AC/DataEnginner-Youtube_Statistics/main/yt.webp)

# Description
This project is a comprehensive data engineering solution designed to automate the process of gathering and analyzing statistics from YouTube channels. By leveraging AWS services and the YouTube API, it streamlines the process from data ingestion to visualization. Here's how it works:

- Data Ingestion: Users upload a .csv file containing YouTube channel IDs to an S3 bucket.
- Triggering Mechanism: An AWS EventBridge event is configured to trigger an AWS Lambda function upon the arrival of the new .csv file.
- Data Processing: The Lambda function reads the channel IDs from the .csv file and uses the YouTube API to fetch statistics for each channel.
- Data Storage: The statistics fetched from the YouTube API are stored in another S3 bucket for persistence.
- Data Transformation and Loading: AWS Glue crawlers are used to catalog the stored data, which is then transformed and loaded into Amazon Athena for querying.
- Visualization: Finally, the data within Athena is connected to Power BI through an ODBC connection, allowing for comprehensive visualization and analysis of the YouTube channel statistics.

# Architecture
![Banner Image](https://raw.githubusercontent.com/CD-AC/DataEnginner-Youtube_Statistics/main/Architecture.png)

# Data Visualization with Power BI
![Banner Image](https://raw.githubusercontent.com/CD-AC/DataEnginner-Youtube_Statistics/main/YouTubeStatsPBI.jpg)
# Features
- Automated Data Collection: Automatically retrieves YouTube channel IDs from a CSV file stored in Amazon S3, enabling seamless data ingestion.
- Serverless Execution: Utilizes AWS EventBridge and Lambda functions for efficient, event-driven processing of YouTube API queries.
- Scalable Data Storage: Stores the queried YouTube statistics in an S3 bucket, ensuring scalable and secure data management.
- Data Transformation and Analysis: Leverages AWS Glue and Athena for robust data crawling, transformation, and query capabilities.
- Advanced Data Visualization: Integrates with Power BI through an Athena ODBC connection, offering powerful visualization and analytics possibilities.
