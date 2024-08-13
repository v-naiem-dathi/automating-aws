import boto3

s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    print("Event:")
    print(event)
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        object_uri = "s3://{0}/{1}".format(source_bucket, key)
        print(object_uri)
        filename = key.replace('source/', '')
        response = transcribe.start_transcription_job(
            TranscriptionJobName=filename,
            LanguageCode='en-US',
            Media={'MediaFileUri': object_uri},
            MediaFormat="mp3",
        )
        print(response)
