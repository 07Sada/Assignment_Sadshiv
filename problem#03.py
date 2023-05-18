import requests
import pandas as pd
import json

# Create a URL object for the JSON file you want to download.
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

# Use the requests.get() method to download the file.
response = requests.get(url)

# Save the file to a local directory.
with open("pokedex.json", "wb") as f:
    f.write(response.content)


json_data = json.load(open("pokedex.json"))

# List containing your dictionaries
dict_list = [json_data["pokemon"][i] for i in range(len(json_data["pokemon"]))]

dict_list_len = len(dict_list)

merged_df = pd.DataFrame()  # Create an empty DataFrame to store the merged result

for i in range(0, dict_list_len):
    dict_i = dict_list[i]  # Fetch the dictionary at index i

    # Make sure the current element is a dictionary
    if isinstance(dict_i, dict):
        df_i = pd.DataFrame.from_dict(dict_i, orient="index").transpose()
        merged_df = pd.concat([merged_df, df_i], axis=0, ignore_index=True)
    else:
        print(f"Skipping element at index {i} as it is not a dictionary.")

# exporting the merged data into excel workbook
merged_df.to_excel("pokemon.xlsx", index=False)
