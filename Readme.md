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

 * *tc_aws.loaders.s3_loader* - takes a S3 key path and optional bucket name, and downloads the file through the S3 API.
 * *tc_aws.loaders.presigning_loader* - instead of downloading via the API, generates a signed link to the file on S3, then feeds it to the Thumbor's regular http loader. This will likely be more performant, as it avoids async issues with the boto library (see [#22](https://github.com/thumbor-community/aws/pull/22) and [#14](https://github.com/thumbor-community/aws/issues/14).
 * *tc_aws.result_storages.s3_storage*
 * *tc_aws.storages.s3_storage*
 
Why use S3-specific loaders rather than just giving the S3 HTTP url to Thumbor? If your S3 files are private and you sign the urls, the query strings will vary and Thumbor will not be able to cache the image.

Additional Configuration values used:

```.ini
# AWS Region the bucket is located in. 
TC_AWS_REGION='eu-west-1' 
# A custom AWS endpoint.
TC_AWS_ENDPOINT=''
# You might need to set this to True for some regions, such as eu-central-1.
S3_USE_SIGV4=False

TC_AWS_STORAGE_BUCKET='' # S3 bucket for Storage
TC_AWS_STORAGE_ROOT_PATH='' # S3 path prefix for Storage bucket

# S3 bucket for Loader. If given, source urls are interpreted as keys
# within this bucket. If not given, source urls are expected to contain
# the bucket name, such as 's3-bucket/keypath'.
TC_AWS_LOADER_BUCKET='' 

# S3 path prefix for Loader bucket. If given, this is prefixed to 
# all S3 keys.
TC_AWS_LOADER_ROOT_PATH=''

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
