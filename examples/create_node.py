import os
import json
from dkan.client import DatasetAPI

uri = os.environ.get('DKAN_URI', False)
user = os.environ.get('DKAN_USER', 'admin')
password = os.environ.get('DKAN_PASSWORD', 'admin')
token = os.environ.get('TOKEN')

print uri, token

if uri:
  api = DatasetAPI(uri, token)
  data = {
      'title': 'Test Dataset',
      'type': 'dataset'
  }
  dataset = api.node('create', data=data)
  print dataset.status_code
  print dataset.text
else:
  print 'Please Set the dkan URL as an ENVIRONMENT variable'
