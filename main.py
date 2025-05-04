# Diana Maldonado
# May 04, 2025
# Homework-Lab10: CSV Student Records

from student_records import Records

# instantiate an object from Records
students = Records('Students.csv')
courses = Records('course enrollment.csv')

# Open file and save data to a list of dictionaries
students_listOfDictionaries = students.load_csv()
courses_listOfDictionaries = courses.load_csv()

# Get count of student per level
std_levels = students.get_levels(students_listOfDictionaries)
students.print_levels(std_levels)

# Get count of units per student
units_list = courses.get_units_per_student(courses_listOfDictionaries)
#print(units_list)

# Ask user for output filename
out_file = input("Enter name of output file: ")

# Output the units per student to the output file
courses.save_to(units_list, out_file)




