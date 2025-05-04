# Diana Maldonado
# April 8, 2025
# Exam 2 

class Person:
  def __init__(self, first, last, gender, age):
    if not isinstance(first, str) or not isinstance(last, str):
      raise TypeError("First and Last names must be strings.")
    if not isinstance(age, int):
      raise TypeError("Age must be an integer")
    if gender not in("male", "female"):
        raise ValueError("Gender must be male or female")
    self.firstname = first
    self.lastname  = last
    self.gender    = gender
    self.age       = age

  def getName(self):
    name = self.firstname + " " + self.lastname 
    print(f"Name = {name}")
    return name
  
  def getGender(self):
    print(f"Gender = {self.gender}")
    return self.gender
  
  def getAge(self):
    print(f"Age = {self.age}")
    return self.age



class CSUF_Student(Person):
  Campus = "CSUF. Go Titans!"
  counter = 0


  def __init__(self, first, last, gender, age):
    super().__init__(first, last, gender, age)
    self._ID = None
    self.major = None
    CSUF_Student.counter += 1

  def set_ID(self, __ID):
    if not isinstance(__ID, str):
      raise TypeError("ID must be a string")
    self.__ID = __ID

  def set_major(self, major):
    if not isinstance(major, str):
      raise TypeError("Major must be a string")
    self.major = major

  def get_ID(self):
    #print(f"ID: {self._ID}")
    return self.__ID
  
  def get_major(self):
    #print(f"Major: {self.major}")
    return self.major 
  
  def get_name(self):
    nameID = f"{super().get_name()} {self.get__ID()}"
    #print(f"Name_ID: {nameID}")
    return nameID #super().getName()
  
  def ChangeMajor(self, major):
    if not isinstance(major, str):
      raise TypeError("Major must be a string")
    self.major = major 
    print(f"Major: {major}")

'''
  def getUnits(self, units):
    if not isinstance(units, str):
      raise TypeError("Units must be a string")
    self.units = units
'''



  
#me = Person(first= "Diana", last= "Maldonado", gender= "female", age=20)
#me.getName()
#print(me.age)
#print(me.gender)
#me2 = CSUF_Student(first= "Joh", last= "Doe", gender= "male", age= 35)
#me2.counter = 1
#print(me2.counter )
#me2.set_ID("1234")
#me2.set_major("CS")
##me2.counter = 1
#me2.getName()
#me2.get_major()
#me2.ChangeMajor("Mathematics")
#me2.get_major()
#print(me2.Campus)
#me2 = CSUF_Student(first= "Di", last= "Mal", gender= "female", age= 35)
#
#print(me2.counter )
