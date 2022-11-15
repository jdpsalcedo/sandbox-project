import logging
import os
from datetime import datetime
from pprint import pprint

import boto3
from botocore.exceptions import ClientError


def append_text(message, file_name, bucket):
    
    # Can create a client
    s3_client = boto3.client('s3')
    # Can also instantiate an S3 resource object
    s3 = boto3.resource('s3')
    object = s3.Object(bucket,file_name)

    try:
        with open('hello_world.txt', 'a') as f:
            f.write('\n'.join([message]))
        object.put(Body = message)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# hello world script to overwrite an s3 object in the sandbox account
message = 'Hello World! The datetime for this upload is {}'.format(datetime.now())
file_name = 'hello_world.txt'
bucket = 'johnsalcedobucket'

append_text(message, file_name , bucket)