import os
import pandas as pd
from flask_cors import CORS

# Load the Excel file
xlsx_file_path = '../БазаОСАстана.xlsx'
df = pd.read_excel(xlsx_file_path, sheet_name='База ОС')

# Extract data from specific columns
selected_columns = ["Фирма", "Наименование", "Тип", "Ответственный"]

# Filter the DataFrame to include only the specified columns
filtered_df = df[selected_columns]

# Filter the DataFrame to include only rows where "Тип" is "Внутренний номер"
filtered_df = filtered_df[(filtered_df['Тип'] == 'Внутренний номер') & (filtered_df['Фирма'] == 'VIAMEDIS')]

# Define the file path for the new Excel and XML files
filtered_xlsx_path = '../filtered_data.xlsx'
filtered_xml_path = '../filtered_data.xml'

# Check if the Excel file exists and delete it
if os.path.exists(filtered_xlsx_path):
    os.remove(filtered_xlsx_path)
    print(f"Deleted existing Excel file: {filtered_xlsx_path}")

# Check if the XML file exists and delete it
if os.path.exists(filtered_xml_path):
    os.remove(filtered_xml_path)
    print(f"Deleted existing XML file: {filtered_xml_path}")

# Save the filtered DataFrame to a new Excel file
filtered_df.to_excel(filtered_xlsx_path, index=False)

print(f"Filtered data has been saved to {filtered_xlsx_path}")

# Create an XML string
xml_data = "<data>\n"
for _, row in filtered_df.iterrows():
    xml_data += "  <item>\n"
    for col_name, cell_value in row.items():
        xml_data += f"    <{col_name}>{cell_value}</{col_name}>\n"
    xml_data += "  </item>\n"
xml_data += "</data>"

# Save the XML string to a file
with open(filtered_xml_path, 'w', encoding='utf-8') as xml_file:
    xml_file.write(xml_data)

print(f"XML data has been saved to {filtered_xml_path}")
