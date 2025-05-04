# Diana Maldonado
# 3/11/25
# Lab 05


import json
import calendar

data = {"20210203075501": {"t": 55, "h": 87, "r": 0}, "20210203090602": {"t": 63, "h": 84, "r": 0}, "20210203102903": {"t": 71, "h": 79, "r": 0}, "20210203125504": {"t": 72, "h": 69, "r": 0}, "20210203183905": {"t": 59, "h": 75, "r": 0}, "20210205044406": {"t": 57, "h": 68, "r": 0.01}, "20210205083307": {"t": 65, "h": 63, "r": 0.05}, "20210205122208": {"t": 73, "h": 56, "r": 0.11}, "20210205161109": {"t": 74, "h": 60, "r": 0.19}, "20210517095510": {"t": 65, "h": 43, "r": 0}, "20210517110611": {"t": 73, "h": 38, "r": 0}, "20210517172912": {"t": 81, "h": 31, "r": 0}, "20210517235513": {"t": 82, "h": 35, "r": 0}, "20210901053914": {"t": 75, "h": 94, "r": 0.05}, "20210901104415": {"t": 81, "h": 89, "r": 0.09}, "20210901153316": {"t": 101, "h": 82, "r": 0.15}, "20210901202217": {"t": 73, "h": 86, "r": 0.23}, "20211126081118": {"t": 69, "h": 32, "r": 0}, "20211126165519": {"t": 73, "h": 27, "r": 0}, "20211126230620": {"t": 63, "h": 20, "r": 0}, "20211126232921": {"t": 62, "h": 24, "r": 0}, "20211225061500": {"t": 34, "h": 2, "r": 0.0}, "20211225123516": {"t": 46, "h": 11, "r": 0.01}, "20220101063039": {"t": 56, "h": 33, "r": 0.0}}


'''
1. All the functions should accept the weather dictionary data structure as follows:
weather dictionary:
   key : datetime as string (formatted as YYYYMMDDhhmmss)
   value : readings dictionary

readings dictionary
   for key : 't'
   value : temperature as integer

   for key : 'h'
   value : humidity as integer

   for key : 'r'
   value : rainfall as float
'''


# weather = {"YYYYMMDDhhmmss": readings}

# readings = {"t": temperature = int, "h": humidity = int, "r": rainfall = float}


#or

# Example weather dictionary with actual values:
# weather = {
#    "20250311123000": {"t": 25, "h": 60, "r": 0.0},
#    "20250311124500": {"t": 26, "h": 58, "r": 0.1}
# }


'''
///////////////////////////////////////////
'''




'''
/////////////// To-Do 1 ////////////////////
Create a weather module.

i. Create a function named read_data which receives a keyword
parameter filename.
a. The function should open the filename in read mode and return a
dictionary of the JSON decoded contents of the file.
b. If the file does not exist, the function should accept the
FileNotFoundError and return an empty dictionary.
'''
def read_data(*, filename):
  """Opens the filename in read mode and returns a dictionary of the JSON decoded contents."""

  # Open filename in read mode.
  try:
    with open(filename, 'r') as file:
      data = json.load(file)
    # return a dictionary of the JSON decoded contents of the file.
    return data

  # If the file does not exist, the function should accept the FileNotFoundError
  except FileNotFoundError:
    # return an empty dictionary.
    return {}
'''
///////////////////////////////////////////
'''




'''
/////////////// To-Do 2 //////////////////
ii. Create a function named write_data which receives a keyword
parameter data (the dictionary) and filename
a. The function should open the filename in write mode and write the
dictionary data into the file encoded as JSON.
'''

def write_data(*, data, filename):
  """Opens a file named filename in write mode and writes the dictionary data into the file encoded as JSON."""


  with open(filename, 'w') as file:
    json.dump(data, file)

  return ' '
'''
///////////////////////////////////////////
'''



'''
/////////////// To-Do 3 /////////////////////
iii. Create a function named max_temperature which receives a keyword
parameter data and date
a. The function should return the maximum temperature for all
dictionary data where the key contains the date as YYYYMMDD.
'''
def max_temperature(*, data, date):
  maxTemp = None
  for key in data:
    if( key[:8] == date):
      current_temp = data[key]['t']
      if maxTemp is None or current_temp > maxTemp:
        maxTemp = current_temp

  return maxTemp

'''
# Alternatively we could use
def max_temperature(*, data, date):
    temps = [reading['t'] for dt, reading in data.items() if dt.startswith(date)]
    return max(temps) if temps else None
'''

'''
///////////////////////////////////////////
'''


'''
///////////// To-Do 4 /////////////////////
iv. Create a function named min_temperature which receives a keyword
parameter data and date
a. The function should return the minimum temperature for all
dictionary data where the key contains the date as YYYYMMDD.
'''

def min_temperature(*, data, date):
  minTemp = None
  for key in data:
    if( key[:8] == date):
      current_temp = data[key]['t']
      if minTemp is None or current_temp < minTemp:
        minTemp = current_temp

  return minTemp

'''
///////////////////////////////////////////
'''


'''
///////////// To-Do 5 /////////////////////
v. Create a function named max_humidity which receives a keyword
parameter data and date
a. The function should return the maximum humidity for all dictionary
data where the key contains the date as YYYYMMDD.
'''

def max_humidity(*, data, date):
  maxHumidity = None
  for key in data:
    if( key[:8] == date):
      current_humidity = data[key]['h']
      if maxHumidity is None or current_humidity > maxHumidity:
        maxHumidity = current_humidity

  return maxHumidity

'''
///////////////////////////////////////////
'''



'''
///////////// To-Do 6 /////////////////////
vi. Create a function named min_humidity which receives a keyword
parameter data and date
a. The function should return the minimum humidity for all dictionary
data where the key contains the date as YYYYMMDD.
'''

def min_humidity(*, data, date):
  minHumidity = None
  for key in data:
    if( key[:8] == date):
      current_humidity = data[key]['h']
      if minHumidity is None or current_humidity < minHumidity:
        minHumidity = current_humidity

  return minHumidity

'''
///////////////////////////////////////////
'''


'''
///////////// To-Do 7 /////////////////////
vii. Create a function named tot_rain which receives a keyword
parameter data and date
a. The function should return the sum of rainfall for all dictionary data
where the key contains the date as YYYYMMDD.
'''
def tot_rain(*, data, date):
  rain_total = 0
  for key in data:
    if( key[:8] == date):
      current_rain = data[key]['r']
      rain_total = rain_total + current_rain

  return rain_total


'''
///////////////////////////////////////////
'''


'''
///////////// To-Do 8 /////////////////////
viii. Create a function named report_daily which receives a keyword
parameter data and date
a. The function should return a single string which when passed to
any print function will display on the screen formatted exactly as
indicated in the example output below. You will most likely be
appending strings together using a literal "\n" where a newline is
desired. To get the month name, you can import the
built in calendar module and call the month_name function passing it
the month as an integer.
'''

def report_daily(*, data, date):
  #output: print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

  line1 = "======================== DAILY REPORT ========================"
  line2 = f"{'Date': <19}  {'Time' : >8}  {'Temperature': <11}  {'Humidity': <8}  {'Rainfall': <9}"
  line3 = f"{'='*19}  {'='*8}  {'='*11}  {'='*8}  {'='*8}"

  header = [line1 , line2 , line3]

  date_str = str(date)
  month = int(date_str[4:6])
  day   = int(date_str[6:8])
  year  = int(date_str[:4])
  index_by_date = f"{calendar.month_name[month]} {day}, {year}"

  for key in sorted(data):
    #if(key[:8] == date):
    if key.startswith(date_str):
      hour = int(key[8:10])
      min = int(key[10:12])
      seconds = int(key[12:14])
      time = f"{hour:02}:{min:02}:{seconds:02}"

      temp = data[key]['t']
      humidity = data[key]['h']
      rainfall = data[key]['r']

      body = f"{index_by_date: <19}  {time: <8}  {temp: >11}  {humidity: >8}  {str(rainfall): >7.2}"
      header.append(body)

  history = "\n".join(header)
  #print(history)
  return history

'''
///////////////////////////////////////////
'''


'''
///////////// To-Do 9 /////////////////////
ix. Create a function named report_historical which receives a keyword
parameter data
a. The function should return a single string which when passed to
any print function will display on the screen formatted exactly as
indicated in the example output below. You will most likely be
appending strings together using a literal "\n" where a newline is
desired. To get the month name, you can import the
builtin calendar module and call the month_name function passing it
the month as an integer.
'''


def report_historical(*, data):
  #output: print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
  #line0 = f"{'Enter date (YYYYMMDDhhmmss): ' }"
  #line1 = f"{'HISTORICAL REPORT': ['='] =38}"
  line1 = "============================== HISTORICAL REPORT ==========================="
  line2a = f"{' '*22}  {'Minimum' : <11}  {'Maximum': <8}  {'Minimum': <8}  {'Maximum': <10}  {'Total': <8}"
  line2b = f"{'Date': <20}  {'Temperature' : <11}  {'Temperature': <11}  {'Humidity': <8}  {'Humidity': <8}  {'Rainfall': <9}"
  line3 = f"{'='*20}  {'='*11}  {'='*11}  {'='*8}  {'='*8}  {'='*8}"

  header = [line1 , line2a , line2b , line3]

  mydate = sorted({key[:8] for key in data})
  for date in mydate:

    month = int(date[4:6])
    day = int(date[6:8])
    year = int(date[:4])
    index_by_date = f"{calendar.month_name[month]} {day}, {year}"

    hour = int(date[8:10])
    min = int(date[10:12])
    seconds = int(date[12:14])
    time = f"{hour}:{min}:{seconds}"

    minTemp = min_temperature( data = data, date = date)
    maxTemp = max_temperature( data = data, date = date )
    minHumid = min_humidity( data = data, date = date )
    maxHumid = max_humidity( data = data, date = date )
    rainTotal = tot_rain( data = data, date = date )


    body = f"{index_by_date: <22}  {minTemp: >11}  {maxTemp: >11}  {minHumid: >11}  {maxHumid: >11}  {rainTotal: >8.2}"
    print(body)
    header.append(body)

  return "\n".join(header)

'''
///////////////////////////////////////////
'''


#report_daily(data=data , date= 20210203075501)
