# Thumbor AWS

[![Join the chat at https://gitter.im/thumbor-community/aws](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/thumbor-community/aws?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Circle CI](https://circleci.com/gh/thumbor-community/aws.svg?style=svg)](https://circleci.com/gh/thumbor-community/aws)

## Installation

```bash
    pip install tc_aws
```

### Authentication

Authentication is handled by botocore, see [Boto3 documentation](https://boto3.readthedocs.org/en/latest/guide/quickstart.html#configuration).

## Origin story

This is a fork of [willtrking thumbor_aws](https://github.com/willtrking/thumbor_aws); as this repository was not maintained anymore,
we decided to maintain it under the [thumbor-community](https://github.com/thumbor-community) organization.

## Contribution

First you need to fork this project.
Clone your repo at your computer
Next, inside a folder for project:

```bash
    make setup
    make test
```

If all test passed, you have an environment ready to start. 
We recommend to use python-virtualevn (virtualenv and virtualenv-wrapper)

## Features

 * tc_aws.loaders.s3_loader
 * tc_aws.loaders.presigning_loader
 * tc_aws.result_storages.s3_storage
 * tc_aws.storages.s3_storage

Additional Configuration values used:

```.ini
TC_AWS_REGION='eu-west-1' # AWS Region

TC_AWS_STORAGE_BUCKET='' # S3 bucket for Storage
TC_AWS_STORAGE_ROOT_PATH='' # S3 path prefix for Storage bucket

TC_AWS_LOADER_BUCKET='' #S3 bucket for loader
TC_AWS_LOADER_ROOT_PATH='' # S3 path prefix for Loader bucket

TC_AWS_RESULT_STORAGE_BUCKET='' # S3 bucket for result Storage
TC_AWS_RESULT_STORAGE_ROOT_PATH='' # S3 path prefix for Result storage bucket
TC_AWS_MAX_RETRY=0 # Max retries for get image from S3 Bucket. Default is 0

# put data into S3 using the Server Side Encryption functionality to
# encrypt data at rest in S3
# https://aws.amazon.com/about-aws/whats-new/2011/10/04/amazon-s3-announces-server-side-encryption-support/
TC_AWS_STORAGE_SSE=False

# put data into S3 with Reduced Redundancy
# https://aws.amazon.com/about-aws/whats-new/2010/05/19/announcing-amazon-s3-reduced-redundancy-storage/
TC_AWS_STORAGE_RRS=False


# Enable HTTP Loader as well?
# This would allow you to load watermarks in over your images dynamically through a URI
# E.g.
# http://your-thumbor.com/unsafe/filters:watermark(http://example.com/watermark.png,0,0,50)/s3_bucket/photo.jpg
TC_AWS_ENABLE_HTTP_LOADER=False

TC_AWS_ALLOWED_BUCKETS=False # List of allowed bucket to be requested
TC_AWS_STORE_METADATA=False # Store result with metadata (for instance content-type)
```
