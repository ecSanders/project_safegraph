#%% Import libraries
import pandas as pd
import numpy as np
import parquet as pq

df = pd.read_parquet(r'C:\Users\ecsan\CSE451\project_safegraph\parquet\popularity_by_day.parquet', engine='pyarrow')

#%% check
df.head(5)
# %%
