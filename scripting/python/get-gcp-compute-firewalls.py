from googleapiclient import discovery 
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = ''
PROJECT_ID = ''

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scope=SCOPES)

compute = discovery.build('compute', 'v1', credentials = credentials)
firewalls = compute.firewalls().list(project=PROJECT_ID).execute()

for rule in firewalls.get('items', []):
    print(rule['name'], rule['network'], rule.get('allowed'))

