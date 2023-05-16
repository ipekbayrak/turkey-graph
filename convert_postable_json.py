import pandas as pd
import json

# Load the Excel file
df = pd.read_excel('türkiye_pos.xlsx', engine='openpyxl')
df.set_index(df.columns[0], inplace=True)

# Convert your Excel file to JSON
data = df.to_json(orient='index')

# Parse the JSON string into a Python dictionary
data_dict = json.loads(data)

# Convert the dictionary back to a JSON string, formatted with indentations
json_data_formatted = json.dumps(data_dict, indent=4,ensure_ascii=False)

# Print the JSON string
print(json_data_formatted)

with open('turkiye_pos.json', 'w' ,encoding='utf-8') as json_file:
    json_file.write(json_data_formatted)