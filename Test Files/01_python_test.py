import numpy as np
import pandas as pd

# Columns represent years
column_header = ['2019','2020',	'2021',	'2022',	'2023',	'2024',	'2025']

# Rows represent Spending Technology Categories
row_header = ['Business Services', 'Hardware', 'IT Services', 'Software', 'Telecom Services']

# Each row in the matrix below represent one Technology and each column one Year of data
test_data = [
    [477.471,	 484.593,	 518.988,	 572.115,	 640.693,	 720.916,	 814.72],
    [2597.189,	2701.082,	3149.978,	3320.256,	3392.421,	3438.651,	3467.47],
    [2600.082,	2628.529,	2896.001,	3286.340,	    None,	4215.841,	4787.348],
    [1556.779,	1654.627,	1831.514,	2025.143,	2237.725,	2481.181,	2762.201],
    [3188.570,	3201.79,	3242.249,	    None,   3355.419,	3402.868,	3444.409]
]

# Propose a solution how to aproximate the mising points

df = pd.DataFrame(test_data, columns=column_header, index=row_header)
df = df.transpose()  # Transpose to make years the index and categories the columns
df.interpolate(method='linear', inplace=True)
df = df.transpose()  # Transpose back to original format
filled_data = df.values.tolist()

# Print the filled data
for i, row in enumerate(filled_data):
    print(f"{row_header[i]}: {row}")