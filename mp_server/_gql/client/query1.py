## https://towardsdatascience.com/connecting-to-a-graphql-api-using-python-246dda927840

import requests
import json
import pandas as pd

# query = """query {
#   ranks {
#     mode
#     name
#     score
#     isMobile
#     regDttm
#   }
# }"""


query = """query {
  ranks {
    mode
    name
    score
  }
}"""


url = 'http://localhost:3000/graphql'
r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)

# if r.status_code == 200:
#     json_data = json.loads(r.text)
#     print(json_data)