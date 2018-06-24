import json
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


headers = {'Content-type': 'application/json','Accept': 'application/json'}


#Get bp spec and resources
url = 'https://10.18.40.96:9440/api/nutanix/v3/blueprints/d59abb18-e2f9-358e-1ddb-c5dfe436e9f9'
resp=requests.get(url, auth=HTTPBasicAuth('admin','P@ssw0rd/4u'), headers=headers, verify=False)
payload=resp.json()
del payload['spec']['name']
del payload['status']
payload['spec']['application_name'] = "DEVOPS_UPTICK"
payload['spec']['app_profile_reference'] = {'kind': 'app_profile', 'uuid':payload['spec']['resources']['app_profile_list'][0]['uuid']}

#if a profile value has to be modified
#payload['spec']['resources']['app_profile_list'][0]['variable_list'][0]['value']="value"

#Post to calm api
url1 = 'https://10.18.40.96:9440/api/nutanix/v3/blueprints/d59abb18-e2f9-358e-1ddb-c5dfe436e9f9/launch'
resp=requests.post(url1, auth=HTTPBasicAuth('admin','P@ssw0rd/4u'), headers=headers, data=json.dumps(payload), verify=False)
print resp.content
