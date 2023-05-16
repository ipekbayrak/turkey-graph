import pandas as pd
import json

# Load the Excel file
df = pd.read_excel('road_lengths.xlsx', engine='openpyxl')

# Set the first column as the index to help with the conversion
df.set_index(df.columns[0], inplace=True)

# Convert the DataFrame to a nested dictionary
# The outer dictionary's keys are the index (city names), and the values are dictionaries
# The inner dictionaries' keys are the column names (city names), and the values are the road lengths
nested_dict = df.to_dict()

#remove nan values
for key in nested_dict:
    nested_dict[key] = {k: v for k, v in nested_dict[key].items() if pd.notnull(v)}
    

# Convert the nested dictionary to a JSON string
json_str = json.dumps(nested_dict,indent=4,ensure_ascii=False)

# Print the JSON string
print(json_str)

# Optionally, write the JSON string to a file
with open('road_lengths.json', 'w',encoding='utf-8') as json_file:
    json_file.write(json_str)
