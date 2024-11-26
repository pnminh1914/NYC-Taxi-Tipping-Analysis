from urllib.request import urlretrieve
import os

# download the data to the landing page
output_relative_dir = './data/landing'

if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)

YEAR = '2023'
MONTHS = range(1, 13)

URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"

# data output directory is `data/landing/`
tlc_output_dir = output_relative_dir

for month in MONTHS:
    # 0-fill i.e 1 -> 01, 2 -> 02, etc
    month = str(month).zfill(2) 
    print(f"Begin month {month}")
    
    # generate url
    url = f'{URL_TEMPLATE}{YEAR}-{month}.parquet'
    
    # generate output location and filename
    output_dir = f"{tlc_output_dir}/{YEAR}-{month}.parquet"
    
    # download
    urlretrieve(url, output_dir) 
    
    print(f"Completed month {month}")

