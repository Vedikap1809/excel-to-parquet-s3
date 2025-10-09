import boto3

class S3Uploader:
    def __init__(self, bucket_name, file_name, s3_path=None):
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.s3_path = s3_path if s3_path else file_name
        self.s3 = boto3.client('s3')

    def upload(self):
        self.s3.upload_file(self.file_name, self.bucket_name, self.s3_path)

if __name__ == "__main__":
    BUCKET_NAME = 'zmx-training-bucketbatch2025'
    FILE_NAME = 'employee.parquet'
    S3_PATH = 'VedikaP/' + FILE_NAME 

    uploader = S3Uploader(BUCKET_NAME, FILE_NAME, S3_PATH)
    uploader.upload()
