#%%
#import psycopg2
#from psycopg2 import sql
import asyncio
import asyncpg

#%%

#conn = psycopg2.connect("host=localhost port=5433")


#%%
#Create a temprary user and data base in the server connection
cursor = conn.cursor()
query = sql.SQL("CREATE USER {username} WITH PASSWORD {password}").format(
    username=sql.Identifier('abcdefgh'),
    password=sql.Placeholder()
)
cursor.execute(query, ('temp_user',))

# %%
