# Transcribing Audio

# Create Transcription Job

After uploading MP3 to S3 bucket, use URL:

s3://nd-acg-transcribe/InauguralAddress-1981.mp3


# Extracting Text

To extract the raw text transcript from the JSON file at the command line:

```sh
jq '.results.transcripts[0].transcript' -r asrOutput.json > transcript.txt
```

More info on `jq` is [here](https://stedolan.github.io/jq/).