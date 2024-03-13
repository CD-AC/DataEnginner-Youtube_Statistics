# Importing necessary libraries for handling data, making HTTP requests, dealing with dates, and interacting with AWS S3
import json
import pandas as pd
import json
import pandas as pd
import time
import requests
import random
import time
import boto3
from datetime import datetime
import datetime
import os

# Initialize the S3 client for interacting with AWS S3
s3_client = boto3.client('s3')

# Constructing the API URL for fetching channel statistics
def get_stats(api_key,channel_id):
    
    url_channel_stats = 'https://youtube.googleapis.com/youtube/v3/channels?part=statistics&id='+channel_id+'&key='+api_key
    response_channels = requests.get(url_channel_stats)
    channel_stats = json.loads(response_channels.content)
    channel_stats = channel_stats['items'][0]['statistics']
    date = pd.to_datetime('today').strftime("%Y-%m-%d")

    data_channel = {

            'Date':date,
            'Total_Views':int(float(channel_stats['viewCount'])),
            'Subscribers':int(float(channel_stats['subscriberCount'])),
            'Video_count':int(float(channel_stats['videoCount']))
                        }

    return data_channel

# Gathers statistics for multiple YouTube channels listed in a DataFrame.
def channels_stats(df,api_key):
    
    date = []
    views = []
    suscriber = []
    video_count = []
    channel_name = []
    
    tiempo = [1,2.5,2]
    
    for i in range(len(df)):
        
        stats_temp = get_stats(api_key,df['Channel_id'][i])
        
        channel_name.append(df['Channel_name'][i])
        date.append(stats_temp['Date'])
        views.append(stats_temp['Total_Views'])
        suscriber.append(stats_temp['Subscribers'])
        video_count.append(stats_temp['Video_count'])
     
    time.sleep(random.choice(tiempo))
    
    data = {
        
        'Channel_name':channel_name,
        'Subscribers':suscriber,
        'Video_count':video_count,
        'Total_Views':views,
        'Createt_at':date,
    }
    
    df_channels = pd.DataFrame(data)
    
    return df_channels

# AWS Lambda function handler to fetch YouTube channels' statistics and store them in AWS S3.
def lambda_handler(event, context):    

    # Retrieving necessary variables from the environment
    bucket_name = os.environ['BUCKET']
    filename =  os.environ['FILE_CHANNELS']
    DEVELOPER_KEY = os.environ['APIKEY']
    
    # Fetching the channels list file from S3 and reading it into a DataFrame
    obj = s3_client.get_object(Bucket=bucket_name, Key= filename)
    df_channels = pd.read_csv(obj['Body'])     
    
    # Generating statistics for all channels
    results = channels_stats(df_channels,DEVELOPER_KEY)
    date = pd.to_datetime('today').strftime("%Y%m%d")
    
    # Saving the results to a temporary CSV file
    results.to_csv(f'/tmp/youtube_stats_{date}.csv',index = False)
 
    # Uploading the CSV file to S3 and cleaning up the temporary file
    s3 = boto3.resource("s3")
    
    s3.Bucket(os.environ['BUCKET_DESTINY']).upload_file(f'/tmp/youtube_stats_{date}.csv', Key=f'youtube_stats_{date}.csv')
    os.remove(f'/tmp/youtube_stats_{date}.csv')

    return f'file youtube_stats_{date}.csv send succeded'
