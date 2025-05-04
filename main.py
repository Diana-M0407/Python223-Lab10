from student_records import Table
from collections import Counter
from typing import List


students = Table('Students.csv')
students_dict = students.load_csv()


#categories = (row["Level"] for row in students_dict)
#counts = Counter(categories)
#print(f"{"="*15}")
#print(f"{counts['FRESH']} freshmen")
#print(f"{counts['SOPH']} sophmores")
#print(f"{counts['JR']} juniors")
#print(f"{counts['SR']} seniors", end="\n\n")

#def get_levels(levels: List[dict[str, int]])->List[dict[str, int]]:
#    grade_levels = (row["Level"] for row in students_dict)
#    return grade_levels

std_levels = students.get_levels(students_dict)
students.print_levels(std_levels)

#def print_levels(std_levels:List[dict[str, int]])-> None:
#    counts = Counter(std_levels)
#    print(f"{"="*15}")
#    print(f"{counts['FRESH']} freshmen")
#    print(f"{counts['SOPH']} sophmores")
#    print(f"{counts['JR']} juniors")
#    print(f"{counts['SR']} seniors", end="\n\n")
#
#    return None


courses = Table('course enrollment.csv')
courses_dict = courses.load_csv()
units_list = courses.get_units_per_student(courses_dict)
print(units_list)


file = input("Enter the name of the file: ")
courses.save_to(file)


#def get_units_per_student(courses: List[dict[str, str]])-> List[dict[str, int]]:
#    
#   #unique_ids = {row["ID"] for row in courses_dict if "ID" in row} 
#
#    # To preserve order in oder of appearance, do a list...
#    unique_ids = list(dict.fromkeys(row["ID"] for row in courses))
#    count_ids = Counter(unique_ids)
#
#    units_per_student: List[dict[str, int]] = []
#
#    for id in unique_ids:
#        tot_units = 0
#        cs_units = 0
#        for row in courses:
#            #print(id)
#            if row["ID"] == id:
#                #print(row)
#                tot_units += int(row['Units'])
#                if row["Course"].startswith("CPSC"):
#                #if row['Course'][:4] == "CPSC":
#                    cs_units += int(row['Units'])
#        student= {"ID":id, "Total Units": tot_units, "CPSC Units": cs_units}
#        units_per_student.append(student)
#    #print(units_per_student)
#        #courses.save_to(id, total_units,CS_units,file)
#        #print(f"{id}: total units: {total_units}, CPSCI units: {CPSCI_units}")
#
#    return units_per_student




