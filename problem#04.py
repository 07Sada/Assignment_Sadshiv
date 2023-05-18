import requests
import pandas as pd
import numpy as np
import json

# Create a URL object for the JSON file you want to download.
url = "https://data.nasa.gov/resource/y77d-th95.json"

# Use the requests.get() method to download the file.
response = requests.get(url)

# Save the file to a local directory.
with open("nasa.json", "wb") as f:
    f.write(response.content)

# load the json data
json_data = json.load(open("nasa.json"))


# create the pandas dataframe
df = pd.DataFrame(json_data, columns=["name", "id", "nametype", "recclass", "mass", "fall", "year", "reclat", "reclong", "geolocation"])

# geolocation column contains dictionary, conterving the series to list
geolocation_list = df['geolocation'].tolist()

# replacing the 'nan' values 
geolocation_list = [{'type': np.nan, 'coordinates': np.nan} if type(item) == float else item for item in geolocation_list]

# creating the dataframe
geolocation_df = pd.DataFrame(geolocation_list)

# merging the dataframe
result = pd.concat([df, geolocation_df], axis=1)

# drop the columns 
result = result.drop(['geolocation', 'type'],axis=1)

# changing the datatypes for the columns
result[["mass", "reclat", "reclong"]] = result[["mass", "reclat", "reclong"]].astype(float)
result['id'] = result['id'].astype(int)
result['year'] = pd.to_datetime(result['year'], format='%Y-%m-%dT%H:%M:%S.%f', errors='coerce')

# exporting the data
result.to_csv('nasa.csv', index=False)