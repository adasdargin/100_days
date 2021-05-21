student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98

#Loop through data frame

#for key, value in student_data_frame.items():
    #print(value)        # not very useful information


# pandas has in-built loop .iterrows()
# loop through rows of data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)        # 56