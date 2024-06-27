import pandas as pd

# Step 1: Read the CSV file
input_file_path = '2018-Central-Park-Squirrel-Census-Squirrel-Data.csv'
df = pd.read_csv(input_file_path)

# Step 2: Calculate the total number of each fur_color
fur_color_counts = df['Primary Fur Color'].value_counts()

# Step 3: Create a new DataFrame with the counts
fur_color_counts_df = fur_color_counts.reset_index()
fur_color_counts_df.columns = ['primary_fur_color', 'count']

# Step 4: Write the new DataFrame to a new CSV file
output_file_path = 'output.csv'
fur_color_counts_df.to_csv(output_file_path, index=False)

print(f"The new data table has been written to {output_file_path}")
