import requests
import pandas as pd
import numpy as np
import json
import pandas as pd
import re

# Create a URL object for the JSON file you want to download.
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Use the requests.get() method to download the file.
response = requests.get(url)

# Save the file to a local directory.
with open("episodes.json", "wb") as f:
    f.write(response.content)

# load the json data
json_data = json.load(open("episodes.json"))

# create a dataframe
df = pd.DataFrame(json_data["_embedded"])

df = pd.DataFrame(df["episodes"].tolist())

# changing the datatype for columns

# updating the datetime format for 'airdate' column
df["airdate"] = pd.to_datetime(df["airdate"])


# Convert the Series to datetime format
airtime_datetime = pd.to_datetime(df["airtime"], format="%H:%M")

# Format the datetime objects into 12-hour time format
airtime_12_hour = airtime_datetime.dt.strftime("%I:%M %p")

df["airtime"] = airtime_12_hour

# changing the runtime format to 'float'
df["runtime"] = df["runtime"].astype(float)

# updating the 'average' column
numerical_values = [
    d["average"] for d in df["rating"] if isinstance(d["average"], (int, float))
]
df["rating"] = numerical_values


# fuction to remove html tags
def remove_html_tags(text):
    clean_text = re.sub("<.*?>", "", text)
    return clean_text


# applying the function on 'summary' column
df["summary"] = df["summary"].apply(remove_html_tags)

# sepearting the medium image link and original image link
df_2 = pd.DataFrame(df["image"].tolist())

# merging the dataframes
result = pd.concat([df, df_2], axis=1)

# selecting the required columns
result = result[
    [
        "id",
        "url",
        "name",
        "season",
        "number",
        "type",
        "airdate",
        "airtime",
        "runtime",
        "rating",
        "summary",
        "medium",
        "original",
    ]
]
result = result.rename(
    columns={
        "medium": "medium_image_link",
        "original": "Original_image_link",
        "rating": "average_rating",
    }
)

# export the dataframe
result.to_csv("episode.csv", index=False)
