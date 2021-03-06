import os
import json
from dkan.client import DatasetAPI

uri = os.environ.get('DKAN_URI', False)
user = os.environ.get('DKAN_USER', 'admin')
password = os.environ.get('DKAN_PASSWORD', 'admin')
token = os.environ.get('TOKEN')

if uri:
  # Make the api authenticate properly
  # api = DatasetAPI(uri, user, password, True)
  api = DatasetAPI(uri, token)

  # List datasets
  params = {
    'parameters[type]': 'dataset',
  }
  r = api.node(params=params)

  print r.json()
else:
  print 'Please Set the dkan URL as an ENVIRONMENT variable'
