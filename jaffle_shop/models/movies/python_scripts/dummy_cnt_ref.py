from sqlalchemy import create_engine
import pandas as pd

# Read 
df=ref('movies_pull')

df_out=pd.DataFrame(df.count())
df_out.columns=['cnt']

write_to_source(df_out,'movies','dummy_cnt')
