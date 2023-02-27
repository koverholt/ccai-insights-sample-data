# ccai-insights-sample-data

Generate sample chat log data in
[CCAI conversation data format](https://cloud.google.com/contact-center/insights/docs/conversation-data-format)
to use in CCAI Insights on Google Cloud, such as:

```json
{
    "entries": [
        {
            "start_timestamp_usec": 1675813229000000,
            "text": "Hello, what can I assist you with?",
            "role": "AGENT",
            "user_id": 2
        },
        {
            "start_timestamp_usec": 1675813258000000,
            "text": "Hi, I'm having an issue with my router",
            "role": "CUSTOMER",
            "user_id": 1
        },
        {
            "start_timestamp_usec": 1675813287000000,
            "text": "Sorry to hear. Can you tell me what the problem is?",
            "role": "AGENT",
            "user_id": 2
        },
        {
            "start_timestamp_usec": 1675813316000000,
            "text": "I have not been able to connect to my account. I cannot log into my account. I cannot access my account. I do not know what to do to fix my account.",
            "role": "CUSTOMER",
            "user_id": 1
        }
    ]
}
```

## Usage

To generate sample chat logs, using the default of 30,000:

```bash
python src/generate-call-logs.py
```

Generate a different number of chat logs, such as 100:

```bash
python src/generate-call-logs.py 100
```

## Uploading to GCS

You can then upload the sample chat log data to Google Cloud Storage (GCS)
using the [`gsutil` tool](https://cloud.google.com/storage/docs/gsutil):

```bash
gsutil -m cp "output/*.json" gs://your-sample-chat-log-bucket
```

## Using Insights

Once you've generated and uploaded the sample data, you can [import the
conversations into CCAI Insights and analyze
them](https://cloud.google.com/contact-center/insights/docs/create-analyze-conversation-ui).
