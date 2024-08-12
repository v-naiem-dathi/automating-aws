# Resizing Images

https://aws.plainenglish.io/easiest-lambda-layers-for-python-functions-357d6dde8c4a

https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html?source=post_page-----357d6dde8c4a--------------------------------#with-s3-tutorial-create-policy

## Create S3 buckets

nd-s3-demo-source-bucket-resized
nd-s3-demo-source-bucket

## Create Policy and Role

## Create the function deployment package

In the same directory in which you created your lambda_function.py file, create a new directory named package and install the Pillow (PIL) library and the AWS SDK for Python (Boto3). Although the Lambda Python runtime includes a version of the Boto3 SDK, we recommend that you add all of your function's dependencies to your deployment package, even if they are included in the runtime. For more information, see Runtime dependencies in Python.

```
mkdir package
pip3 install \
--platform manylinux2014_x86_64 \
--target=package \
--implementation cp \
--python-version 3.12 \
--only-binary=:all: --upgrade \
pillow boto3
```
