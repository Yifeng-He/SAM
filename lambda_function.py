import pandas as pd
import boto3
import io

s3_client = boto3.client('s3')

def load_csv(s3_client, bucket, key, sep = ','):
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    df_data = pd.read_csv(io.BytesIO(obj['Body'].read()),  sep=sep)
    return df_data

def lambda_handler(event, context):
    bucket = event['Bucket']
    key = event['Key']
    
    df = load_csv(s3_client, bucket, key)
    list_cols = list(df.columns)
    print('test')
    print(list_cols)
    
    return list_cols
