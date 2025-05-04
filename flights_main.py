# Diana Maldonado
# April 29, 2025
# Lab09- Tuffy Flight Schedule


import json
from flights import Flights
import atexit
from pathlib import Path

list_of_flights = Flights("Titan Flight schedule.json")
atexit.register(lambda: Path(list_of_flights.filename).unlink(missing_ok = True))


'''
f1 = list_of_flights.add_flight(
    "IAD",            # Ontario, CA
    "LHR",            # San Francisco, CA
    "1",
    "2200",
    "Y",
    "0530"
)

f2 = list_of_flights.add_flight(
    "LAX",            # Ontario, CA
    "ord",            # San Francisco, CA
    "545",
    "1230",
    "n",
    "1640"
)

f3 = list_of_flights.add_flight(
    "ord",            # Ontario, CA
    "cle",            # San Francisco, CA
    "409",
    "1733",
    "N",
    "1857"
)

f4 = list_of_flights.add_flight(
    "CLE",            # Ontario, CA
    "IAD",            # San Francisco, CA
    "83",
    "1953",
    "N",
    "2119"
)

f5 = list_of_flights.add_flight(
    "IAD",            # Ontario, CA
    "LHR",            # San Francisco, CA
    "1",
    "2200",
    "Y",
    "0530"
)

f5 = list_of_flights.add_flight(
    "LHR",            # Ontario, CA
    "LAX",            # San Francisco, CA
    "2222",
    "2350",
    "Y",
    "2201"
)

'''




while True:
      print("""
        *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU\n
1. Add flight 
2. Print flight schedule
3. Set flight schedule filename
9. Exit the program
      """)

      try:
          choice = int(input("Enter menu choice: "))

      except ValueError:
          print( "Invalid input! Please enter a number.")
          continue

      if choice == 1:
        #Add flight 
        orig = input("Enter origin: ")
        dest = input("Enter destination: ")
        num = input("Enter flight number: ")
        depart= input("Enter departure time (HHMM): ")
        arrival = input("Enter arrival time (HHMM): ")
        nextDay = input("Is arrival next day (Y/N): ")
        myFlight = list_of_flights.add_flight(orig, dest, num, depart, nextDay, arrival)
        

      elif choice == 2:
        #Print flight schedule
        print(f"\n{'='*20} FLIGHT SCHEDULE {'='*20}")
        print(f"{'Origin':6}  {'Destination':11}  {'Number':6}  {'Departure':9}  {'Arrival':7} {'Duration':8}")
        print(f"{'='*6}  {'='*11}  {'='*6}  {'='*9}  {'='*8} {'='*8}")
        #for item in list_of_flights.data:
        for flight in list_of_flights.get_flights():
          o, d, n, dep, arr, dur, = flight
          #name = f"{item.firstname} {item.lastname}"
          #duration = "2"
          #print(f"{item['origin']:6}  {item['destination']:11}  {item['flight_number']:>6}  {item['departure']:>9}  {item['arrival']:>7} {item[dur]:>8}")
          print(f"{o:6}  {d:11}  {n:>6}  {dep:>9}  {arr:>8} {dur:>8}")

      elif choice == 3:
        #Set flight schedule filename 
        file_name = input("Enter filename: ")
        list_of_flights = Flights(file_name)

      
#      # To keep file data instead...
#      elif choice == 3:     
#        # ask for new name                             
#        new_name = input("Enter new filename: ")
#
#        # persist current data to that file
#        with open(new_name, "w", encoding="utf-8") as f:
#          json.dump(list_of_flights.data, f, indent=2)
#
#        # update the object in place
#          list_of_flights.filename = new_name
#          print("Schedule saved as", new_name)
      


      elif choice == 9:
          print("Exiting program. Goodbye!")
          atexit.register(lambda: Path(list_of_flights.filename).unlink(missing_ok = True))
          break

      else:
          print("Invalid choice. Please enter a number between 1 and 4, or 9 to exit.")

