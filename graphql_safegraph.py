# %%
# https://pypi.org/project/safegraphQL/
# import sys
# !{sys.executable} -m pip install safegraphQL
# %%
# import sys
# !{sys.executable} -m pip install --pre gql
# %%
import os
from dotenv import load_dotenv
load_dotenv()
sfkey = os.environ.get("SAFEGRAPH_KEY")
# %%
# https://pypi.org/project/safegraphQL/
# https://github.com/echong-SG/API-python-client-MKilic
import requests
import json
import pandas as pd
import safegraphql.client as sgql

# %%
# https://gql.readthedocs.io/en/v3.0.0a6/
# https://github.com/graphql-python/gql
# Please note that this basic example won't work if you have an asyncio event loop running. In some python environments (as with Jupyter which uses IPython) an asyncio event loop is created for you. In that case you should use instead the async usage example.
# 
# import asyncio
# https://gql.readthedocs.io/en/latest/async/async_usage.html#async-usage
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# %%

# %%
# Select your transport with a defined url endpoint
transport = RequestsHTTPTransport(
    url="https://api.safegraph.com/v1/graphql",
    verify=True,
    retries=3,
    headers={'Content-Type': 'application/json', 'apikey': sfkey})

# %%
async with Client(transport=transport,  
    fetch_schema_from_transport=True
    ) as client:
        result = await client.execute(query)
# %%
client = Client(transport=transport, fetch_schema_from_transport=True)
# %%
query = """
query {
  lookup(placekey: "225-222@5vg-7gs-t9z"){
    placekey
    safegraph_core {
      location_name
      region
      postal_code
    }
  }
}
"""

# %%
results = client.execute(query)
# %%
url = 'https://api.safegraph.com/v1/graphql'

r = requests.post(
    url,
    json={'query': query},
    params = {'apikey':sfkey})

# %%
print(r.status_code)
print(r.text)
# %%
json_data = json.loads(r.text)
# %%
df_data = json_data['data']['characters']['results']
df = pd.DataFrame(df_data)
# %%

# %%
sgql_client = sgql.HTTP_Client(apikey = sfkey)

# %%
pks = [
    'zzw-222@8fy-fjg-b8v', # Disney World 
    'zzw-222@5z6-3h9-tsq'  # LAX
]
cols = [
    'location_name',
    'street_address',
    'city',
    'region',
    'postal_code',
    'iso_country_code'
]

sgql_client.lookup(product = 'core', placekeys = pks, columns = cols)
# %%
sgql_client.lookup(product = 'core', placekeys = pks, columns = "*")

# %%
geo = sgql_client.lookup(product = 'geometry', placekeys = pks, columns = '*')
patterns = sgql_client.lookup(product = 'monthly_patterns', placekeys = pks, columns = '*')

# %%
watterns = sgql_client.lookup(product = 'weekly_patterns', placekeys = pk, columns = '*')

# %%
## weekly patterns
dates = ['2019-06-15', '2019-06-16', '2021-05-23', '2018-10-23']

sgql_client.lookup(
    product = 'weekly_patterns', 
    placekeys = pks, 
    date = dates, 
    columns = ['placekey', 'location_name', 'date_range_start', 'date_range_end', 'raw_visit_counts']
)
# %%
dates = {'date_range_start': '2019-04-10', 'date_range_end': '2019-06-05'}

watterns = sgql_client.lookup(
    product = 'weekly_patterns', 
    placekeys = pks, 
    date = dates, 
    columns = ['placekey', 'location_name', 'date_range_start', 'date_range_end', 'raw_visit_counts']
)

core = sgql_client.lookup(product = 'core', placekeys = pks, columns = ['placekey', 'location_name', 'naics_code', 'top_category', 'sub_category'])
geo = sgql_client.lookup(product = 'geometry', placekeys = pks, columns = ['placekey', 'polygon_class', 'enclosed'])

# %%
merged = sgql_client.sg_merge(datasets = [core, geo, watterns])
# %%
# look-up by name
# https://github.com/echong-SG/API-python-client-MKilic#lookup_by_name