class Person:
  def __init__(self, first, last):
    if not isinstance(first, str) or not isinstance(last, str):
      raise TypeError("First and Last names must be strings.")
    self.firstname = first
    self.lastname = last


class Faculty(Person):
  def __init__(self, first, last, department):
    super().__init__(first, last)
    self.department = department

class Student(Person):
  def __init__(self, first, last):
    super().__init__(first, last)
    self.classyear = None
    self.major = None
    self.advisor = None


  def set_class(self, year):
    if not isinstance(year, str):
      raise TypeError("Class year must be a string")
    self.classyear = year

  def set_major(self, major):
    if not isinstance(major, str):
      raise TypeError("Major must be a string")
    self.major = major

  def set_advisor(self, advisor):
    if not isinstance(advisor, Faculty):
      raise TypeError("Advisor must be a Faculty object")
    self.advisor = advisor
