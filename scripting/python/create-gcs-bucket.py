from google.cloud import storage

client = storage.Client.from_service_account_json('')
bucket = client.bucket('my-secure-bucket123')
bucket.location = 'US'
bucket.create()

bucket.iam_configuration.uniform_bucket_level_access_enabled = True
bucket.patch() 

print("Bucket created with uniform access enabled")