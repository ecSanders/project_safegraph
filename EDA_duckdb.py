# %%
import pandas as pd
import duckdb
import os

# import pyarrow as pa
# import pyarrow.parquet as pq
# %%
con = duckdb.connect(database='chipotle_july.duckdb', read_only=False)
# %%
con.execute("SHOW TABLES").fetchall()
# %%
vh = con.execute("SELECT * FROM visitor_home_cbgs").fetchdf()
# %%
