import json
from datetime import datetime

import boto3
from botocore.exceptions import NoCredentialsError

bucket_name = 'stewmart-email-checker'


def upload_to_aws(email_id: str, data: dict):
    s3 = boto3.client('s3')
    key = datetime.now().strftime(f'{email_id}__%m-%d-%Y%__H%M%')

    try:
        s3.put_object(
            Body=json.dumps(data).encode('UTF-8'),
            Bucket=bucket_name,
            Key=key
        )
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': key
            },
            ExpiresIn=24 * 3600
        )
        return url
    except NoCredentialsError:
        print("Credentials not available")
        return None
