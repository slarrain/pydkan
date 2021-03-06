import os
import json
from dkan.client import DatasetAPI

uri = os.environ.get('DKAN_URI', False)
user = os.environ.get('DKAN_USER', 'admin')
password = os.environ.get('DKAN_PASSWORD', 'admin')
token = os.environ.get('TOKEN')

if uri:
  # api = DatasetAPI(uri, user, password, True)
  api = DatasetAPI(uri, token)
  data = {
      'title': 'Test Dataset',
      'type': 'dataset'
  }
  dataset = api.node('create', data=data)
  print dataset.status_code
  print dataset.text
  nid = dataset.json()['nid']
  op = api.node('delete', node_id=nid)
  print op.status_code
  print op.text
else:
  print 'Please Set the dkan URL as an ENVIRONMENT variable'
