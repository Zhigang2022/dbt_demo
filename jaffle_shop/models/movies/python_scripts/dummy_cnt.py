from sqlalchemy import create_engine
import pandas as pd

user='myusername'
password='mypassword'
db_string = f"postgresql://{user}:{password}@127.0.0.1:5432/"


db_engine = create_engine(db_string)
db_connection=db_engine.connect()



# Read 
sql='''
select *
from "myusername"."public_dbt"."movies"
'''
df=pd.read_sql(sql,db_connection)

df_out=pd.DataFrame(df.count())
df_out.columns=['cnt']

df_out.to_sql('dummy_cnt',db_connection,schema='public_dbt',if_exists='replace')
