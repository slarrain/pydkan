import os
import json
from dkan.client import DatasetAPI

#specify your DKAN_URI you are posting to here, e.g. 'http://docs.digital.mass.gov/'
uri = os.environ.get('DKAN_URI', False)
# user = os.environ.get('DKAN_USER', 'admin')
# password = os.environ.get('DKAN_PASSWORD', 'admin')
token = "put your service token here"

if uri:
  #api = DatasetAPI(uri, user, password, True)
  api = DatasetAPI(uri, token, True)
  payload = {'parameters[type]': 'resource'}
  nodes = api.node(params=payload).json()
  resource = nodes[0]
  print resource
  #csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.',
  #                   'data', 'tension_sample_data.csv')
  #specify the file you want to post to the resource node you are updating here.
  csv = full_path = os.path.expanduser('~/Downloads/sample_test_data.csv')
  # Attach the file to the resource node
  r = api.attach_file_to_node(csv, resource['nid'], 'field_upload')
  print r.status_code
  print r. text
  #specify the node id of the resource/item you are posting to, e.g. 'node_id=771'
  resource = api.node('retrieve', node_id=resource['nid'])
  print resource.json()['field_upload']
else:
  print 'Please Set the dkan URL as an ENVIRONMENT variable'  
