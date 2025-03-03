import pandas as pd

# Load the Parquet file
df = pd.read_parquet("yellow_tripdata_2023-02.parquet")

# Print the first data point
print(df.iloc[0])
