import pandas as pd

# Path to the input text file
input_file = 'SAF_MYW_20240428.txt'

# Read the text file using pandas read_csv
df = pd.read_csv(input_file, header=None)

# Rename the columns to Column1, Column2, ...
df.columns = [f'Column{i+1}' for i in range(df.shape[1])]

# Path to the output Excel file
output_file = 'output.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)

print(f"Data has been saved to {output_file}")