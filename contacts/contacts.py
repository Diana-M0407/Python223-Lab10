# Diana Maldonado
# March 22, 2025
# Homework-Lab06

import json

class Contacts:
  def __init__(self,*, filename = "contacts.json"):
    self.filename = filename
    self.data = {}
    try:
      with open(self.filename, 'r') as file:
        self.data = json.load(file)
    except FileNotFoundError:
      # File doesn't exit yet, so we start with an empty contact list
      self.data = {}




  def add_contact(self, *, id, first_name, last_name):
    # id key already exits, return "erro"
    if id in self.data:
      print("Phone number already exists.")
      return "error"

    #else, set key:value pair--> id:[first_name, last_name]
    self.data[id] = [first_name, last_name]


    # Sort the data dictionary by last name, then first name (both case-insensitive)
    sorted_data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
    self.data = sorted_data

    # Write new sorted data into file
    with open(self.filename, 'w') as file:
      json.dump(self.data, file, indent=4)

    print(f"Added: {first_name} {last_name}.")
    return {id:[first_name, last_name]}




  def modify_contact(self, *, id, first_name, last_name):
    if id not in self.data:
      print("Invalid phone number")
      return "error"

    self.data[id]=[first_name, last_name]

    #sort dictionary by last name then by fist name (both case insensitive)
    sorted_data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
    self.data = sorted_data

    with open(self.filename, 'w') as file:
      json.dump(self.data, file, indent=4)

    print(f"Modified: {first_name} {last_name}.")
    return {id:[first_name, last_name]}




  def delete_contact(self, *, id):
    if id not in self.data:
      print("Invalid phone number.")
      return "error"

    #pair = self.data[id]
    deleted = {id: self.data[id]}
    del self.data[id]

    with open(self.filename, 'w') as file:
      json.dump(self.data, file, indent=4)

    print(f"Deleted: {deleted[id][0]} {deleted[id][1]}.")
    return deleted
