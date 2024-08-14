# Triggering Lambda from SQS

## Sending messages to SQS

Run the provided script `send_message.py` to send messages to SQS

**Example**: Send a message containing random text to the `Messages` queue every 0.1 second (10 messages per second):

```sh
chmod + x ./send_message.py
./send_message.py -q Messages -i 0.1
```

Press `Ctrl+C` to quit.

Creating Table and SQS Queue can be done manually.
The lambda has to be created with the trigger.

## Create DynamoDB Table

```sh
aws dynamodb create-table --table-name Message \
  --attribute-definitions AttributeName=MessageId,AttributeType=S \
  --key-schema AttributeName=MessageId,KeyType=HASH \
  --billing-mode=PAY_PER_REQUEST
```

## Create SQS Queue

```sh
aws sqs create-queue --queue-name Messages
```
