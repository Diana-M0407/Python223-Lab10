'''
Hello everyone,

Like I mentioned in class the CSV Reader or DictReader objects act as iterators... in another words after creating them you can loop through them right away:

myReader=csv.reader(file)
for row in myReader:
     #process each row of the file

When this goes through all the iterations of the loop, you're at the end of the file and so you cannot do another loop through the reader object.  
Before doing that you will either have to re-open the file and re-create a reader object or 
use the file object's seek() method to move the 'cursor' to the beginning of the file:  file.seek(0)

Please take a note of this, in case your solution involves writing more than one loop for a given reader or dictReader object.


**************************************************************************************************************************
**************************************************************************************************************************
Students.csv - This file includes "ID", "level" and "major" of several students.  There are no duplicate IDs in this file:
                ID   : int
                level: FRESH, SOPH, JR, SR
                major: CPSCI

                ID,Level,Major
                ===============
                152,FRESH,CPSCI
                142,FRESH,CPSCI
                121,SR,CPSCI
                112,FRESH,CPSCI

****************************************************************************************************************************
****************************************************************************************************************************
Course enrollments.csv - This file includes the classes that the students in the students.csv file are taking this semester.  
                         The columns are "ID", "Course" and "Units":
                         ID    : int
                         Course: CPSC, OTHER 
                         Units : int
                    
                         ID,Course,Units
                         ===============
                         152,HCOM100,3
                         152,CPSC121A,2
                         152,CPSC121L,1

****************************************************************************************************************************


Please write a Python program to (using the given above 2 files) print the number of freshmen, sophomores, juniors and 
seniors to the output window: 
    
    ============
    15 freshmen
    14 sophmores
    25 juniors
    41 seniors
*****************************************************************************************************************************
'''






'''
****************************************************************************************************************************************
The program also has to create an output CSV file that includes the total number of units, as well as the total number of CPSC 
units (courses that start with 'CPSC') each student is taking. The ID field in this file is unique.  'Total Units' and 'CPSC Units' are 
the sum of all units and all the Computer Science classes units the student is taking, respectively.  The output file is to have 3 
columns: ID, Total Units and CPSC Units:
    
    ID,Total Units,CPSC Units
    =========================
    152,14,3
    142,18,0
    121,18,12
    112,13,3
    126,13,9
    ...

Your output CSV file should include all 95 students.  Please test your program before submitting and submit (submit only the 
program). 
*****************************************************************************************************************************************
'''

# Diana Maldonado
# April 29, 2025
# Lab09- Tuffy Flight Schedule

#from __future__ import annotations

#import json
from collections import Counter
import re
from pathlib import Path
from typing import List, Tuple, Dict, Union

_TIME_RE = re.compile(r"(?:[01]\d|2[0-3])[0-5]\d")

import os, csv

class Table:
    def __init__(self, filename: str)-> None:
        self.filename:str = filename
        #self.data = List[Tuple[int, str, str]] = []
        #self.data = List[Dict[str, Union[int, str]]] = []
        self.data = []

    def load_csv(self)-> List[dict[int, str,str]]:
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"No such file: {self.filename!r}")

        with open(self.filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            # convert reader to a list of dicts
            self.data = list(reader)
            #print(self.data)

            # each row is a dict: {header1: value1, header2: value2, header3: value3}
        #for id_str, str_1, str_2 in self.data:
        #for row in self.data:
                # e.g. {'id': '152', 'level': 'SOPH', 'Major': 'CPSCI '}
         #   print(row)
         #   print(f"{id_str}, {str_1}, {str_2}")
                #self.data.append((int(id_str), str_1, str_2))
        return self.data
    
    def get_levels(self, levels: List[dict[str, int]])->List[dict[str, int]]:
        grade_levels = (row["Level"] for row in levels)
        return grade_levels

    def add_courses(self, ID: int, Total_Units: int, CPSC_Units: int, filename: str)-> bool:
        
        row = {
            "ID"          : ID,
            "Total Units" : Total_Units,
            "CPSC Units"  : CPSC_Units,
            }
        
        #self.data.append(row)

        with open(filename, "w", encoding= "utf-8") as f:
           fieldnames = ["ID", "Total Units", "CPSC Units"]
           writer = csv.writer(f, fieldnames = fieldnames)
           writer.writerheader()
           writer.writerow(self.data)
            
        # return true if flight added and json written
        return True    
    
    def get_units_per_student(self, courses: List[dict[str, str]])-> List[dict[str, int]]:
        unique_ids = list(dict.fromkeys(row["ID"] for row in courses))
        #count_ids = Counter(unique_ids)

        units_per_student: List[dict[str, int]] = []

        for id in unique_ids:
            tot_units = 0
            cs_units = 0
            for row in courses:
                #print(id)
                if row["ID"] == id:
                    #print(row)
                    tot_units += int(row['Units'])
                    if row["Course"].startswith("CPSC"):
                    #if row['Course'][:4] == "CPSC":
                        cs_units += int(row['Units'])
            student= {"ID":id, "Total Units": tot_units, "CPSC Units": cs_units}
            units_per_student.append(student)
        #print(units_per_student)
            #courses.save_to(id, total_units,CS_units,file)
            #print(f"{id}: total units: {total_units}, CPSCI units: {CPSCI_units}")
        return units_per_student


    def save_to(self, in_file:List[dict[str, int]], out_filename: str) -> None:
        with open(out_filename, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            # (optional) write a header row if you want
            writer.writerow(["ID", "Total Units", "CPSC Units"])

            # write each dict as a simple list of values
            for row in in_file:
                writer.writerow([
                    row["ID"],
                    row["Total Units"],
                    row["CPSC Units"],
                ])
   
    def print_levels(self, std_levels:List[dict[str, int]])-> None:
        counts = Counter(std_levels)
        print(f"{"="*15}")
        print(f"{counts['FRESH']} freshmen")
        print(f"{counts['SOPH']} sophmores")
        print(f"{counts['JR']} juniors")
        print(f"{counts['SR']} seniors", end="\n\n")
    
        return None
    
    # Helper function
    @staticmethod
    def _verify_time(hhmm: str) -> bool:
        #returns True if time format is correct
        return bool(_TIME_RE.fullmatch(hhmm))

    def add_flight(self, origin: str, destination: str, flight_number: str, departure: str , next_day: str, arrival:str)-> bool:
        #origin        = origin
        #destination   = destination
        #flight_number = flight_number

        if not self._verify_time(departure):
            return False

        if not self._verify_time(arrival):
            return False
        
        if next_day not in ("Y", "N", "y", "n"):
            return False
        
        self.data.append(  
            {
            "origin"       : origin.upper(),
            "destination"  : destination.upper(),
            "flight_number": flight_number.upper(),
            "departure"    : departure,
            "next_day"     : next_day.upper(),
            "arrival"      : arrival,
            }
        )

        #with open(self.filename, "w", encoding= "utf-8") as f:
        #   json.dump(self.data, f, indent=2)
            
        # return true if flight added and json written
        return True

    # Helper functions: 
    @staticmethod
    def _HHMM_to_minutes(HHMM: str):
        return int(HHMM[:2])*60 + int(HHMM[2:])
    
    @staticmethod
    def _minutes_to_HHMM(mins: int):
        h, m = divmod(mins, 60)
        return f"{h}:{m:02d}"
    
    @staticmethod
    def _format_ampm(HHMM: str):
        h, m = int(HHMM[:2]), int(HHMM[2:])
        ampm = "am" if h < 12 else "pm"
        h12 = h % 12 or 12
        return f"{h12}:{m:02d}{ampm}"
    
    def get_flights(self):
        display : list[tuple[str, str, str, str, str, str]] = []

        for f in self.data:
            depart_ampm = self._format_ampm(f["departure"])
            arrival_plus = f["next_day"] == "Y"
            arrival_ampm = ("+" if arrival_plus else '') + self._format_ampm(f["arrival"])

            mins = self._HHMM_to_minutes(f["arrival"]) - self._HHMM_to_minutes(f["departure"])
            if arrival_plus:
                mins += 24*60
            dur = self._minutes_to_HHMM(mins)

            display.append(
                (
                f["origin"],
                f["destination"],
                f["flight_number"],
                depart_ampm, arrival_ampm, dur,
                )
            )

        return display


#record = Table("Students.csv")
#record.load_csv()
