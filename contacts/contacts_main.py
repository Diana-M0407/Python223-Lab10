# Diana Maldonado
# March 22, 2025
# Homework-Lab06

from contacts import Contacts

def main():

  with open("contacts.json",'w') as file:
    file.write("{}")

  Titan_list = Contacts(filename = "contacts.json")

  while True:
      print("""
        *** TUFFY TITAN CONTACT MAIN MENU\n
1. Add contact
2. Modify contact
3. Delete contact
4. Print contact list
5. Set contact filename
6. Exit the program
      """)

      try:
          choice = int(input("Enter menu choice: "))

          if 0> choice <=6:
              continue

          elif choice > 6:
              print("Invalid choice. Please enter a number between 1 and 6.")

          else:
              pass

      except ValueError:
          choice = 0
          print( "Invalid input! Please enter a number between 1 and 6.")


      if choice == 1:
          try:
              phone_number = int(input("\nPlease enter your phone number: "))

              if type(phone_number) is int:
                  first = input("Enter fist name: ")
                  last = input("Enter last name: ")
                  Titan_list.add_contact(id=phone_number, first_name = first, last_name = last)

          except ValueError:
              print( "Invalid input! Please enter a number a valid phone number.")
              phone_number = 0
              choice = 0
              pass


      elif choice == 2:
          try:
              phone_number = int(input("\nPlease enter your phone number: "))

              if type(phone_number) is int:
                  first = input("Enter fist name: ")
                  last = input("Enter last name: ")
                  Titan_list.modify_contact(id=phone_number, first_name = first, last_name = last)

          except ValueError:
              print( "Invalid input! Please enter a valid phone number.")
              phone_number = 0
              choice = 0
              pass


      elif choice == 3:
          try:
              phone_number = int(input("\nPlease enter your phone number: "))

              if type(phone_number) is int:
                  Titan_list.delete_contact(id = phone_number)

          except ValueError:
              print( "Invalid input! Please enter a valid phone number.")
              phone_number = 0
              choice = 0
              pass


      elif choice == 4:
        print(f"\n{'='*20} CONTACT LIST {'='*20}")
        print(f"{'Last Name':20}  {'First Name':20}  {'Phone':10}")
        print(f"{'='*20}  {'='*20}  {'='*10}")
        for number, name in Titan_list.data.items():
            print(f"{name[1]:20}  {name[0]:20}  {number:10}")

      elif choice == 5:
          filename = input("\nPlease enter the filename: ")
          Titan_list.__init__(filename = filename)
          print(f"Filename: {filename}.")


      elif choice == 6:
          print("Goodbye!")
          break

      else:
          pass

if __name__== "__main__":
    main()
