# speech-to-srt
Speech to SRT example

## Environment Vars
```
export PROJECT_ID=
```

## Authentication

### Create Service Account
```
gcloud iam service-accounts create speech-to-srt --display-name="Speech to Text Service Account"
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:speech-to-srt@$PROJECT_ID.iam.gserviceaccount.com --role roles/ml.developer
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:speech-to-srt@$PROJECT_ID.iam.gserviceaccount.com --role roles/viewer
gcloud projects add-iam-policy-binding $PROJECT_ID --member serviceAccount:speech-to-srt@$PROJECT_ID.iam.gserviceaccount.com --role roles/storage.objectAdmin
```
### Create a GCs Bucket
```
gcloud config set project $PROJECT_ID
gsutil mb -p $PROJECT_ID -c regional -l europe-west2 gs://rocketech-de-pgcp-sandbox-speech-to-srt-source
```

### Create Service Account Key
> This is required because the Speech to Text API is not yet supported by the user credentials
```
gcloud iam service-accounts keys create ./speech-to-srt.json --iam-account speech-to-srt@$PROJECT_ID.iam.gserviceaccount.com
```

### GOOGLE_APPLICATION_CREDENTIALS
```
export GOOGLE_APPLICATION_CREDENTIALS=./speech-to-srt.json
```

## To convert a WAV file to FLAC
This is required in order to use the Speech to Text API

```
brew install libav
```

Convert