import boto3 #type: ignore

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

file_name = "/Users/saketshokeen/Desktop/intershipt/Python_Learning/api.py"
object_name = "api.py"
bucket = "devopssaipowered"

response = s3.Bucket(bucket).upload_file(file_name, object_name)

print("File uploaded successfully!")

def upload_to_s3(file_name, object_name, bucket):
    
    response = s3.Bucket(bucket).upload_file(file_name, object_name)

    return response.json()