from sqlalchemy import create_engine
import pandas as pd

# Read 
df=ref('movies_pull')

write_to_source(df,'movies','movies_pull')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
print(f"{bcolors.WARNING} The movies_pull.py script has been used as final part of movies_pull. {bcolors.ENDC}")
