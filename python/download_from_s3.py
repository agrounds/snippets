import boto3
from os import environ


def main():
    session = boto3.Session(
        aws_access_key_id=environ.get('ACCESS_KEY'),
        aws_secret_access_key=environ.get('SECRET_KEY'),
    )
    s3 = session.resource('s3')

    obj = s3.Object('some-bucket', 'some/path/key.txt')
    obj.download_file('~/tmp/file.txt')

    dest = s3.Object('some-bucket2', 'some/destination/file.txt')
    dest.copy({
        'Bucket': 'some-bucket',
        'Key': 'some/path/key.txt',
    })


if __name__ == '__main__':
    main()
