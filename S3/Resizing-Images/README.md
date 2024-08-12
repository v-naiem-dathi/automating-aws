# Resizing Images

https://aws.plainenglish.io/easiest-lambda-layers-for-python-functions-357d6dde8c4a

https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html?source=post_page-----357d6dde8c4a--------------------------------#with-s3-tutorial-create-policy

## Create S3 buckets

nd-s3-demo-source-bucket-resized
nd-s3-demo-source-bucket

## Create Policy and Role

- Create permissions policy from JSON

- To create an execution role and attach your permissions policy (console)
    - Open the Roles page of the (IAM) console.
    - Choose Create role.
    - For Trusted entity type, select AWS service, and for Use case, select Lambda.
    - Choose Next.
    - Add the permissions policy you created in the previous step by doing the following:
    - In the policy search box, enter created Policy name and select the check box for that policy.
    - Choose Next.
    - Under Role details, for the Role name enter LambdaS3Role.
    - Choose Create role.

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

To create your test event, in the Test event pane, do the following:

Under Test event action, select Create new event.
- For Event name, enter myTestEvent.
- For Template, select S3 Put.
- Replace the values for the following parameters with your own values.
    - For awsRegion, replace us-east-1 with the AWS Region you created your Amazon S3 buckets in.
    - For name, replace amzn-s3-demo-bucket with the name of your own Amazon S3 source bucket.
    - For key, replace test%2Fkey with the filename of the test object you uploaded to your source bucket in the step Upload a test image to your source bucket.