from elasticsearch import Elasticsearch
from random import randint
import json


es = Elasticsearch(
  ['lp01.idea.rpi.edu:443/elasticsearch'],
  # turn on SSL
  use_ssl=True,
  # no verify SSL certificates
  verify_certs=False,
  # don't show warnings about ssl certs verification
  ssl_show_warn=False
)

# create a Python dictionary for the search query:
search_param = {
  "_source": True,
  "query": {
    "filter" : {
            "exists" : {
               "field" : "in_reply_to_status_id_str"
            }
    }
  }
}

es_index = 'coronavirus-data-all'

# helper methods to see which 
def printMappings():
  # print out searchable indexes in elasticsearch
  mapping = es.indices.get_mapping(es_index)
  with open('mapping.json', 'w') as f:
    f.write(json.dumps(mapping))

# method for continuously gathering all tweets per search
def search():
  response = []
  
  # perform a search for 2ms and get initial index
  page = es.search(index=es_index, 
                       scroll='2m',
                       size = 1000,
                       search_type='scan',
                       body=search_param)
  scroll_id = page['_scroll_id']
  scroll_size = page['hits']['total']
  response.extend(page['hits']['hists'])
  
  # Start scrolling until we have all documents that match our query
  while (scroll_size > 0):
    page = es.scroll(scroll_id = scroll_id, scroll = '2m')
    # Update the scroll ID
    scroll_id = page['_scroll_id']
    # Get the number of results that we returned in the last scroll
    scroll_size = len(page['hits']['hits'])
    response.extend(page['hits']['hists'])
  return response

if __name__ == '__main__':
  search()


