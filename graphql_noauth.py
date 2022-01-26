# %%
# https://towardsdatascience.com/connecting-to-a-graphql-api-using-python-246dda927840
import requests
import json
import pandas as pd
# %%
query = """
query {
    characters {
    results {
      gender
      name
      status
      species
      type
      image
      origin {
        dimension
        created
      }
      episode {
        episode
        name
        air_date
      }
    }
  }
}

"""
# %%
url = 'https://rickandmortyapi.com/graphql/'
r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)
# %%
json_data = json.loads(r.text) # b\c its a string
# %%
df_data = json_data['data']['characters']['results']
df = pd.DataFrame(df_data)
# %%
df
# %%
