import glob
import ipaddr
import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class cloudService:
    name: str
    properties: dict

temp_path = glob.glob('./ServiceTags_*.json')[0]

with open(temp_path, 'r', encoding='utf-8') as json_read_file:
    jsonPlan = json.loads(json_read_file.read())

    for item in jsonPlan['values']:
        if item['name'] == 'AzureCloud':
            azureCloudService = cloudService(item['name'], item['properties'])

    print('\n============================================================\n')
    print(' Comparing AzureCloud service tag with other cloud services.\n')
    print(' Any Azure service tag listed below with an IP address is')
    print('                NOT found in the AzureCloud.\n')
    print('============================================================\n')

    for item in jsonPlan['values']:
        if item['name'] != 'AzureCloud':
            result = False
            task = cloudService(item['name'], item['properties'])
            for addressPrefix in task.properties['addressPrefixes']:
                for cloudAddressPrefix in azureCloudService.properties['addressPrefixes']:
                    n1 = ipaddr.IPNetwork(cloudAddressPrefix)
                    n2 = ipaddr.IPNetwork(addressPrefix)
                    if n1.version == n2.version:
                        result = n1.overlaps(n2)
                        if result == True:
                            break
            if result == False:
                print(item['name'])
                print(n2,"\n")