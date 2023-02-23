# ccai-insights-sample-data

Generate sample chat log data in
[CCAI conversation data format](https://cloud.google.com/contact-center/insights/docs/conversation-data-format)
to use in CCAI Insights on Google Cloud.

## Usage

To generate sample chat logs, using the default of 10,000:

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
gsutil -m cp output/* gs://your-sample-chat-log-bucket
```

## Using Insights

Once you've generated and uploaded the sample data, you can [import the
conversations into CCAI Insights and analyze
them](https://cloud.google.com/contact-center/insights/docs/create-analyze-conversation-ui).
