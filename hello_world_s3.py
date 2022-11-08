import logging
import os
from datetime import datetime
from pprint import pprint

import boto3
from botocore.exceptions import ClientError


def append_text(message, file_name, bucket):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

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