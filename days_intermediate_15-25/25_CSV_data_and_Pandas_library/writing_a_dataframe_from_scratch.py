import pandas

# Create a dataframe from scratch
data_dct = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

df_data = pandas.DataFrame(data_dct)
print(df_data)
#   students  scores
# 0      Amy      76
# 1    James      56
# 2   Angela      65

df_data.to_csv("creating_new_csv_file.csv")
