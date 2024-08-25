import duckdb
from wurlitzer import pipes
from utils import generate_sql
from llama_cpp import Llama
import os

os.environ['CMAKE_ARGS'] = "-DLLAMA_METAL=on"

with pipes() as (out, err):
    client = Llama(
        model_path="externalfiles/DuckDB-NSQL-7B-v0.1-q8_0.gguf",
        n_ctx=2048,
    )

con = duckdb.connect("externalfiles/nyc.duckdb")

question = "get most recent tpep_pickup_datetime from taxi table starting with 'a'"

sql_query = generate_sql(question, con, client)

print(sql_query)
