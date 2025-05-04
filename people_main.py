# Diana Maldonado
# March 31, 2025
# Homework-Lab07

from people import Student, Faculty
from person import*

'''
Faculty_list = [
Faculty ("Susan", "Barua","Computer Science"),
Faculty( "Hosssen", "Moini", "Mechanical Engineering"),
Faculty("Huda", "Munjy", "Civil Engineering"),
Faculty("Mostafa", "Shiva","Electrical Engineering"),
Faculty ("George", "Kiran","Computer Engineering")
]
'''

Faculty_list = []
Student_list = []

while True:
      print("""
        *** TUFFY TITAN STUDENT/FACULTY MAIN MENU\n
1. Add faculty
2. Print faculty
3. Add student
4. Print student
9. Exit the program
      """)

      try:
          choice = int(input("Enter menu choice: "))

      except ValueError:
          print( "Invalid input! Please enter a number.")
          continue

      if choice == 1:
        #Add faculty
        first = input("Enter fist name: ")
        last = input("Enter last name: ")
        department = input("Enter department: ")
        faculty = Faculty(first, last, department)
        Faculty_list.append(faculty)

      elif choice == 2:
        #Print faculty
        print(f"\n{'='*23} FACULTY {'='*23}")
        print(f"{'Record':6}  {'Name':20}  {'Department':25}")
        print(f"{'='*6}  {'='*20}  {'='*25}")
        for i, item in enumerate(Faculty_list):
          name = f"{item.firstname} {item.lastname}"
          print(f"{i:<6}  {name:20}  {item.department:25}")


      elif choice == 3:
        #Add student
        first = input("Enter fist name: ")
        last = input("Enter last name: ")
        year = input("Enter class year: ")
        major = input("Enter major: ")

        if not Faculty_list:
           print("No faculty in list. Please add faculty first.")
           continue

        try:
           index = int(input("Enter faculty advisor: "))
           faculty = Faculty_list[index]

        except (ValueError, IndexError):
          print( "Invalid input! Please enter a number.")
          continue

        #for idx, adv in enumerate(Faculty_list):
        #   if idx == index:
        #      faculty = Faculty(adv.firstname, adv.lastname, adv.department)

        student = Student(first, last)
        student.set_class(year)
        student.set_major(major)
        student.set_advisor(faculty)
        Student_list.append(student)


      elif choice == 4:
        #Print student
        print(f"\n{'='*37} STUDENTS {'='*37}")
        print(f"{'Name':20}  {'Class':8}  {'Major':25}  {'Advisor':25}")
        print(f"{'='*20}  {'='*8}  {'='*25}  {'='*25}")
        for s in Student_list:
            name = f"{s.firstname} {s.lastname}"
            advisor = f"{s.advisor.firstname} {s.advisor.lastname}"
            print(f"{name:20}  {s.classyear:8}  {s.major:25}  {advisor:25}")


      elif choice == 9:
          print("Exiting program. Goodbye!")
          break

      else:
          print("Invalid choice. Please enter a number between 1 and 4, or 9 to exit.")
