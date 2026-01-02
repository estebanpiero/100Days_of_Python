# Dictionary Comprehension with Pandas
# new_dict = {new_key:new_value for item in list}

import pandas

student_dic = {
    'student': ['Angela','James','Lily'],
    'score':[56,76,98]    
}

student_data_frame = pandas.DataFrame(student_dic)

# Looping through a DataFrame to create a dictionary
# Looping through rows of a DataFrame

for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
    