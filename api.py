from system_utils import get_system_health
from fastapi import FastAPI #type: ignore
import boto3 #type: ignore
s3 = boto3.resource('s3')
app = FastAPI(title="DevOps Utilities API")

@app.get("/hello")
def hello():
    return {"message": "Hello, Friends from DevOps Utilities API!"} 

@app.get("/metrics")
def metrics():
    '''
    this API endpoint will return the system health metrics like CPU, Memory and Disk usage,etc
    '''
    return get_system_health()

@app.get("aws/s3/buckets")
def list_s3_buckets():
    '''
    this API endpoint will return the list of all S3 buckets in the AWS account
    '''
    buckets = []
    for bucket in s3.buckets.all():
        print(bucket.name)

    