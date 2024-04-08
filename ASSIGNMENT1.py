"""Perform the following operations using R/Python on suitable data sets:
a) read data from different formats (like csv, xls)
b) indexing and selecting data, sort data,
c) describe attributes of data, checking data types of each column,
d) counting unique values of data, format of each column, converting variable data type (e.g.
from long to short, vice versa),
e) identifying missing values and fill in the missing values"""

import pandas as pd

data = pd.read_csv("DSMLlab/admission.csv")

"""id_number = input("Enter ID number: ")
selected_data = data[data["Serial No."] == int(id_number)]

if len(selected_data) > 0:
    column_number = int(input("Enter column number: (GRE score = 2, TOEFL score = 3, University rating = 4, SOP = 5, LOR = 6, CGPA = 7, Reseacrh = 8, Chance of admit = 9)"))
    if column_number > 0 and column_number <= len(selected_data.columns):
        specific_cell = selected_data.iloc[0, column_number-1]
        print(f"{selected_data.iloc[0,column_number-1:column_number]}")
    else:
        print("Invalid column number. Please enter a number between 1 and", len(selected_data.columns))
else:
    print("No data found for the given ID number.")"""

sorted_data = data.sort_values(by="CGPA", ascending=False)

sorted_data.to_csv("DSMLlab/sorted.csv", index=False)

attributes = data.columns.tolist()
"""for col in attributes:
    format = str(data[col].dtype)
    print(f"{col}: {format}")"""

data_types = data.dtypes.tolist()

"""for i in range(len(column_heads)):
    print(f"{column_heads[i]}: {str(data_types[i])}")"""

unique_values = [data[col].nunique() for col in attributes]

"""for i in range(len(column_heads)):
    print(f"{column_heads[i]}: {unique_values[i]} unique values")"""

missing_values = data.isnull().sum()
for column, value in missing_values.items():
    if value > 0:
        print(f"Column '{column}' has {value} missing values.")