import csv

csv_columns = ['Id', 'Course', 'Duration', 'Teacher']
dict_data = [
    {'Id': 1, 'Course': 'Python', 'Duration': '4 Weeks', 'Teacher': 'Mr.Krishna'},
    {'Id': 2, 'Course': 'JavaScript', 'Duration': '5 Weeks', 'Teacher': 'Mr.Hassan'},
    {'Id': 3, 'Course': 'React', 'Duration': '12 Weeks', 'Teacher': 'Mr.Dash'},
    {'Id': 4, 'Course': 'Java', 'Duration': '8 Weeks', 'Teacher': 'Mr.Charan'},
    {'Id': 5, 'Course': 'Php', 'Duration': '6 Weeks', 'Teacher': 'Mrs.Muna'},
]

with open("courses.csv", 'w') as course_csv:
    writer = csv.DictWriter(course_csv, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)