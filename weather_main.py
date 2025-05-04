# Diana Maldonado
# 3/11/25
# Lab 05

#Import the weather module.
import weather
import re

_TIME_RE = re.compile(r"(?:[01]\d|2[0-3])[0-5]\d")

#Set a default filename to store the JSON data. 
filename = "weather_data.json"

#Declare a dictionary to hold the weather data.
hows_the_weather = {}


data = {"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}, "20210517095510": {"t": 65, "h": 43, "r": 0}, "20210517110611": {"t": 73, "h": 38, "r": 0}, "20210517172912": {"t": 81, "h": 31, "r": 0}, "20210517235513": {"t": 82, "h": 35, "r": 0}, "20210901053914": {"t": 75, "h": 94, "r": 0.05}, "20210901104415": {"t": 81, "h": 89, "r": 0.09}, "20210901153316": {"t": 101, "h": 82, "r": 0.15}, "20210901202217": {"t": 73, "h": 86, "r": 0.23}, "20211126081118": {"t": 69, "h": 32, "r": 0}, "20211126165519": {"t": 73, "h": 27, "r": 0}, "20211126230620": {"t": 63, "h": 20, "r": 0}, "20211126232921": {"t": 62, "h": 24, "r": 0}, "20211225061500": {"t": 34, "h": 2, "r": 0.0}, "20211225123516": {"t": 46, "h": 11, "r": 0.01}, "20220101063039": {"t": 56, "h": 33, "r": 0.0}}

def main():

  
  #Set a default filename to store the JSON data. 
  filename = "weather_data.json"

  #Declare a dictionary to hold the weather data.
  hows_the_weather = {}


while True:
      print("""
        *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU\n
1. Set data filename
2. Add weather data
3. Print daily report
4. Print historical report
9. Exit the program
      """)


      try:
          choice = int(input("Enter menu choice: "))

      except ValueError:
          print( "Invalid input! Please enter a number.")
          continue

      if choice == 1:
        #Set data filename
        file_name = input("Enter data filename: ")
        #Using the return value set the weather data dictionary.
        hows_the_weather = weather.read_data(filename)
        

      elif choice == 2:

        date = input("Enter date (YYYYMMDD): ").strip() 
        time = input("Enter time (hhmmss): ").strip()

        # Helper function
        @staticmethod
        def _verify_time(hhmm: str) -> bool:
          #returns True if time format is correct
          return bool(_TIME_RE.fullmatch(hhmm))

        if not _verify_time(time):
          #return False
          print(f"Invalid time input (hhmm)!")
          continue

        temperature = int(input("Enter temperature: ")) #int
        if temperature is not isinstance(temperature, int):
          raise TypeError("Temperature must be of an integer")
        humidity = int(input("Enter humidity: "))  #int
        if not isinstance(humidity, int):
           raise TypeError("humidity must be an integer")
        rainfall = float(input("Enter rainfall: "))  #float
        if not isinstance(rainfall, int):
           raise TypeError("rainfall must be an integer")
        


        input_key = date + time
        hows_the_weather[input_key] = {'t': temperature, 'h': humidity, 'r': rainfall}

        weather.write_data( data = hows_the_weather, filename= filename)


      elif choice == 3:
        #Print daily report
        date = input("Enter date (YYYYMMDD): ").strip() #string
        #Call the weather report_daily function.
        if len(date) < 8:
          print("date must be YYYYMMDD form.")
          continue
        daily = weather.report_daily( data = hows_the_weather, date = date)
        print(daily)    #Print out the return string.
      

      elif choice == 4:
        #Print historical report
        #Call the weather report_historical function.
        historical = weather.report_historical(data= hows_the_weather)
        print(historical)   #Print out the return string.

      elif choice == 9:
        #Exit the program
        print("Goodbye!\n")
        break
      
      else:
          print("Invalid choice. Please enter a number between 1 and 4, or 9 to exit.")

if __name__ == "__main__":
      main()













'''
def menu():
    print("""

          *** EMPLOYEE CONTACT MAIN MENU\n
    1. Set data filename
    2. Add weather data
    3. Print daily report
    4. Print historical report
    9. Exit the program
    """)


while True:
    menu()
    mychoice = input("Enter menu choice: ").strip()
    try:
        choice = int(mychoice)

    except ValueError:
        #if invalid choice is entered, prompt the user for valid number
        choice = 0
        print( "Invalid input! Please enter a number between 1-4, 9: ")
        print('You entered', choice)


    if choice == 1:
    

    elif choice == 2:
      date = input("Enter date (YYYYMMDD): ").strip() #string
      time = input("Enter time (hhmmss): ").strip() #string

      try:
            temperature = int(input("Enter temperature: ")) #int
            humidity = int(input("Enter humidity: "))  #int
            rainfall = float(input("Enter rainfall: "))  #float

      except ValueError:
            #if invalid choice is entered, prompt the user for valid number
            print( "Invalid input! Please enter valid numbers for temperature, humidity, and rainfall. ")                                
            phone_number = 0
            choice = 0
            continue

            input_key = date + time
            hows_the_weather[input_key] = {'t': temperature, 'h': humidity, 'r': rainfall}

            weather.write_data( data = hows_the_weather, filename= filename)



    elif choice == 3:
      date = input("Enter date (YYYYMMDD): ").strip() #string
      daily = weather.report_daily( data = hows_the_weather, date = date)
      print(daily)



    elif choice == 4:
      historical = weather.report_historical(data= hows_the_weather)
      print(historical)


    elif choice == 9:
      #Exit the program
      print("Goodbye!\n")
      break


    else:
      print("invalid choice. Please try again.")


if __name__ == "__main__":
      main()
'''
